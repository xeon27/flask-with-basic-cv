import os
from flask import render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from app import app
from app.forms import QueryForm, ImageForm, ViewForm
from app.utils import get_num_words, transform_img, modify_filename


@app.route("/")
@app.route("/index")
def index():
    user = {"username": 'Omkar'}
	
    return render_template('index.html', title='Home', user=user)
    

@app.route("/query", methods=['GET', 'POST'])
def query():
    form = QueryForm()
    if form.validate_on_submit():
        flash('Your query consists of {} words'.format(get_num_words(form.query.data)))
        return redirect(url_for('query'))
    return render_template('query.html', title='Query', form=form)
    

@app.route("/image", methods=['GET', 'POST'])
def image():
    form = ImageForm()
    if form.validate_on_submit():
        # Get file
        f = form.image.data
        
        # Secure name of file
        filename = secure_filename(f.filename)
        
        # Save file
        image_dir = os.path.join(os.getcwd(), app.config['IMAGE_FOLDER'])
        f.save(os.path.join(image_dir, filename))
        
        return redirect(url_for('view', filename=filename))
    
    return render_template('image.html', title='Upload Image', form=form)
    

@app.route("/image/view/<filename>", methods=['GET', 'POST'])
@app.route("/image/view/<filename>/<ext>", methods=['GET', 'POST'])
def view(filename, ext=None):
    form = ViewForm()
    file_ext = None
    if form.validate_on_submit():
        if 'gray' in request.form:
            file_ext = transform_img(app.config['IMAGE_FOLDER'], filename, 0)            
        
        return redirect(url_for('view', filename=filename, ext=file_ext))
            
    return render_template('view.html', title='View Image', filename=modify_filename(filename, ext), form=form)
    


        
        
        
        
    
    