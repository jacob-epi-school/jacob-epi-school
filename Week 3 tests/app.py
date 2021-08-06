from flask import Flask, render_template, url_for, redirect, abort


app = Flask(__name__)

@app.context_processor
def inject_hello():
    return dict(userId=['77', 'jacob', 'jacob@jacob.com'])


@app.route('/<int:n>')
def start(n):
    try:
        if(n == 100):
            return redirect(url_for('enter_cave'))

        title = "The Counterintuitive Cave"

        picture_url = url_for("static", filename="cave_entrance.jpg")
        
        text = """You walk up to a cave and there is a sign that reads, "Your expectations may defy reality."
        You are intrigued, but you also can sense the danger that lurks inside. What do you do?"""

        choices = [
            ('enter_cave',"Go inside"),
            ('run_away',"Run away as fast as you can!!!")
        ]

        return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=picture_url)
    except Exception as err:
        return redirect(url_for('error', err = err))

@app.route('/error/<err>')
def error(err):
    try:
        return render_template('error.html', errMsg = err)
    except:
        abort(418)

@app.route('/creepy')
def enter_cave():
    title = "You go inside..."
    
    picture_url = url_for("static", filename="sword_stone.jpg")

    text = """... and a fog rolls in that makes it impossible to see the exit. You see in front of you 
    a sword stabbed into a rock. This would be a great way to defend yourself from any danger in the cave.
    The sense of impending doom looms larger. What do you do?"""

    choices = [
        ('go_deeper',"Go deeper into the cave"),
        ('escape_cave',"Try to escape the way you came from"),
        ('sword_pickup',"Pick up the sword in the rock")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=picture_url)



@app.route('/whatsgoingon')
def escape_cave():
    title = "You turn back to get away..."
    
    picture_url = url_for("static", filename="sword_stone.jpg")

    text = """...but the more and more you walk, you start to realize you should've gotten out by now. You walk
    a bit further and find that sword in the rock again. You could've sworn you were walking in a straight line
    and that you went the exact way you came from, but you ended up in the same place as before. What do you do?"""

    choices = [
        ('go_deeper',"Turn and go deeper into the cave"),
        ('escape_cave',"Keep going towards the mouth of the cave"),
        ('sword_pickup',"Pick up the sword in the rock")
    ]

    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=picture_url)



@app.route('/mimicssuck')
def sword_pickup():
    title = "Look out!"
    
    picture_url = url_for("static", filename="honedge.png")

    text = """As you go to take the sword out, you find out this is no ordinary sword. It leaps out of
    the rock and swiftly attacks; decapitating you. Your adventure is over, but oh well, you'll make
    a good feast."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=picture_url)



@app.route('/youthought')
def run_away():
    title = "You run away..."

    picture_url = url_for("static", filename="fallen_tree.jpg")
    
    text = """...but as you do a storm rolls in and a lightning bolt strikes a huge tree directly. The tree
    falls and smashes you. Your adventure is over, but look at the bright side, you are now skinnier than
    a sheet of paper."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=picture_url)



@app.route('/howdoesthiswork')
def go_deeper():
    title = "You go deeper into the cave"

    picture_url = url_for("static", filename="Victory.jpg")
    
    text = """As you go you start to see a light off in the distance. You go towards it and find the mouth
    of the cave. You are not quite sure how it happened, but you are just glad you got out of that evil and
    confusing cave. Your adventure is now over. You may have gotten nothing from it, but just be glad you are
    in one piece."""

    choices = []

    return render_template('adventure.html', title=title, text=text, choices=choices, picture_url=picture_url)