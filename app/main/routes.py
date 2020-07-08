import os
from flask import render_template, flash, redirect, url_for, request
from werkzeug.utils import secure_filename
from app import app
from app.main import bp
from app.main.forms import QueryForm, ImageForm, ViewForm
from app.main.utils import get_num_words, transform_img, modify_filename
    
    
@bp.route("/", methods=['GET', 'POST'])
@bp.route("/index", methods=['GET', 'POST'])
def index():
    form = ImageForm()
    if form.validate_on_submit():
        # Get file
        f = form.image.data
        
        # Secure name of file
        filename = secure_filename(f.filename)
        
        # Save file
        image_dir = os.path.join(os.getcwd(), app.config['IMAGE_FOLDER'])
        f.save(os.path.join(image_dir, filename))
        
        flash('Your image was uploaded!')
        return redirect(url_for('main.view', filename=filename))
    
    return render_template('index.html', title='Upload Image', form=form)
    

@bp.route("/index/view/<filename>", methods=['GET', 'POST'])
@bp.route("/index/view/<filename>/<ext>", methods=['GET', 'POST'])
def view(filename, ext=None):
    form = ViewForm()
    file_ext = None
    if form.validate_on_submit():
        if 'gray' in request.form:
            file_ext = transform_img(app.config['IMAGE_FOLDER'], filename, 0)    
        elif 'edgev' in request.form:
            file_ext = transform_img(app.config['IMAGE_FOLDER'], filename, 1)
        elif 'edgeh' in request.form:
            file_ext = transform_img(app.config['IMAGE_FOLDER'], filename, 2)
        
        return redirect(url_for('main.view', filename=filename, ext=file_ext))
            
    return render_template('view.html', title='View Image', filename=modify_filename(filename, ext), form=form)
    
    
@bp.route("/about")
def about():
    user = {"username": 'Omkar'}
	
    return render_template('about.html', title='About Me', user=user)
    
    
@bp.route("/query", methods=['GET', 'POST'])
def query():
    form = QueryForm()
    if form.validate_on_submit():
        flash('Your query consists of {} words'.format(get_num_words(form.query.data)))
        return redirect(url_for('main.query'))
    return render_template('query.html', title='Query', form=form)
    


        
        
        
        
    
    