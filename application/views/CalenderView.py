from flask_classful import FlaskView, route
from flask import render_template, request, redirect, url_for

events = [
    {
        'title' : 'TestEvent',
        'start' : '2022-06-25', 
        'end' : '',
        'url' : 'https://youtube.com'
    },
    {
        'title' : 'Another TestEvent',
        'start' : '2022-06-25', 
        'end' : '2022-06-26',
        'url' : 'https://google.com'
    },
]

class CalenderView(FlaskView):
    @route('/add', methods=['GET', 'POST'])
    def add(self):
        if request.method == "POST":
            title = request.form.get('title')
            start = request.form.get('start')
            end = request.form.get('end')
            url = request.form.get('url')
            if end == '':
                end=start
            events.append({
            'title' : title,
            'start' : start,
            'end' : end,
            'url' : url},)
            return redirect(url_for('CalenderView:add'))
        else:
            return render_template("add.html")

    @route('/cal')
    def cal(self):
        return render_template('cal.html', events=events)