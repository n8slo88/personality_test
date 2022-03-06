from flask import Flask, render_template, url_for, request
from flask_bootstrap import Bootstrap
import pandas

df = pandas.read_csv(r'templates/questionstwo.csv')
questions = df.to_dict(orient="index")

app = Flask(__name__)
Bootstrap(app)

phlegscore=[0]
choscore=[0]
melscore=[0]
sanscore=[0]
num=[0]
choleric=[ 1, 3, 5, 8, 11, 14, 15, 25, 30, 36, 37, 38, 42, 43, 44, 50, 53,
54, 56, 60, 66, 67, 73, 81, 83, 84, 86, 90, 92, 96, 105, 108, 112, 115,
116, 117, 118, 121, 123, 124, 125, 127, 130, 132, 133, 134, 135, 138,
140, 143, 144, 154, 155, 156, 157, 158, 167, 168, 172, 176, 177, 183,
191, 192, 194, 196, 200, 207, 209, 213, 218, 219, 222, 224, 227]

phlegmatic=[ 2, 4, 6, 9, 10, 21, 26, 28, 30, 31, 35, 39, 45, 52, 55, 58, 61,
63, 64, 65, 68, 70, 72, 75, 78, 85, 88, 97, 98, 100, 102, 103, 106, 107,
110, 111, 113, 119, 122, 126, 128, 129, 131, 137, 139, 147, 153, 160,
162, 166, 169, 171, 173, 174, 175, 185, 186, 188, 189, 195, 198, 199,
201, 204, 205, 206, 210, 211, 215, 217, 219, 221, 225, 226, 228, 232]

sanguine=[ 1, 3, 5, 9, 10, 11, 14, 17, 18, 23, 26, 29, 30, 32, 36, 37,
38, 41, 43, 46, 47, 48, 49, 50, 56, 59, 68, 69, 71, 76, 77, 79, 80, 82,
87, 89, 91, 92, 93, 94, 95, 104, 107, 110, 112, 113, 114, 116, 117,
118, 120, 121, 129, 131, 136, 138, 139, 142, 144, 145, 146, 148,
149, 152, 157, 159, 160, 161, 175, 178, 179, 180, 203, 206, 212,
214, 220, 223, 226, 228, 230, 231]

melancholic=[ 2, 7, 8, 12, 13, 16, 19, 20, 21, 22, 24, 27, 28, 31, 33,
34, 39, 40, 42, 48, 51, 52, 54, 57, 62, 63, 70, 72, 73, 74, 75, 78, 79,
80, 81, 88, 98, 99, 101, 106, 109, 111, 122, 131, 133, 141, 150,
151, 153, 159, 163, 165, 166, 170, 173, 176, 181, 182, 184, 186,
187, 190, 193, 197, 202, 204, 208, 210, 215, 216, 221, 222, 227]

@app.route('/', methods=['GET', 'POST'])
def start():
        if request.method =="POST":
            move_one()
            question=questions[num[0]]['question']
            post_id=num[0]
            if post_id in phlegmatic:
                phlegadd_one()
                return render_template("index.html",post_id=post_id, post=question,sanscore=sanscore[0], phlegscore=phlegscore[0], choscore=choscore[0],melscore=melscore[0])
            elif post_id in choleric:
                choadd_one()
                return render_template("index.html",post_id=post_id, post=question,sanscore=sanscore[0], choscore=choscore[0], phlegscore=phlegscore[0], melscore=melscore[0])
            elif post_id in melancholic:
                meladd_one()
                return render_template("index.html",post_id=post_id, post=question,sanscore=sanscore[0], choscore=choscore[0], phlegscore=phlegscore[0], melscore=melscore[0])
            elif post_id in sanguine:
                sanadd_one()
                return render_template("index.html",post_id=post_id, post=question,sanscore=sanscore[0], choscore=choscore[0], phlegscore=phlegscore[0], melscore=melscore[0])
            else:
                return render_template("index.html", post_id=post_id, post=question, phlegscore=phlegscore[0],
                                       sanscore=sanscore[0], choscore=choscore[0], melscore=melscore[0])

        else:
            move_one()
            post_id=num[0]
            question=questions[num[0]]['question']
            return render_template("index.html",post_id=post_id, post=question, phlegscore=phlegscore[0], sanscore=sanscore[0], choscore=choscore[0], melscore=melscore[0])

def sanadd_one():
    score_int = sanscore[0]
    new_score = score_int + 1
    sanscore[0] = new_score

def meladd_one():
    score_int = melscore[0]
    new_score = score_int + 1
    melscore[0] = new_score

def phlegadd_one():
    score_int=phlegscore[0]
    new_score=score_int+1
    phlegscore[0]=new_score

def choadd_one():
    score_int=choscore[0]
    new_score=score_int+1
    choscore[0]=new_score

def move_one():
    ques_int=num[0]
    new_num=ques_int+1
    num[0]=new_num




if __name__ == "__main__":
    app.run(debug=True)