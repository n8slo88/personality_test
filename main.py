from flask import Flask, render_template, url_for, request, jsonify
from flask_bootstrap import Bootstrap
import pandas

df = pandas.read_csv(r'templates/questionstwo.csv')
questions = df.to_dict(orient="index")

app = Flask(__name__)
Bootstrap(app)


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

melancholic=[2,7,8,12,13,16,19,20,21, 22,24,27,28,31,33,34,
 39,40,42,48,51,52,54,57,62,63,70,72,73,74, 75, 78, 79,
80, 81, 88, 98, 99, 101, 106,109,111,122,131,133,141,150,
151, 153, 159, 163, 165, 166,170,173,176,181,182,184,186,
187, 190, 193, 197, 202, 204,208,210,215,216,221,222,227]

score_=[0]
num=[0]
sscore_=[0]
mscore_=[0]
pscore_=[0]
cscore_=[0]
bnum=[0]

@app.route('/')
def index():
     onum=bnum[0]
     return render_template('index.html', onum=onum)


@app.route('/b', methods=['GET','POST'])
def indexb():
      onum=1
      post_id=num[0]
      if post_id in melancholic and request.method == "POST":
          if post_id in phlegmatic:
              m_plus()
              mscore = mscore_[0]
              p_plus()
              pscore = pscore_[0]
              move_one()
              output = questions[num[0]]['question']
              post_id = num[0]
              return {'output': output, 'post_id': post_id, 'mscore': mscore, 'pscore': pscore}
          elif post_id in choleric:
              m_plus()
              mscore = mscore_[0]
              c_plus()
              cscore = cscore_[0]
              move_one()
              output = questions[num[0]]['question']
              post_id = num[0]
              return {'output': output, 'post_id': post_id, 'mscore': mscore, 'cscore': cscore}
          elif post_id in sanguine:
              m_plus()
              mscore = mscore_[0]
              s_plus()
              sscore = sscore_[0]
              move_one()
              output = questions[num[0]]['question']
              post_id = num[0]
              return {'output': output, 'post_id': post_id, 'mscore': mscore, 'sscore': sscore}
          else:
              m_plus()
              mscore = mscore_[0]
              move_one()
              output = questions[num[0]]['question']
              post_id = num[0]
              return {'output': output, 'post_id': post_id, 'mscore': mscore}

      elif post_id in phlegmatic and request.method == "POST":
          if post_id in sanguine:
              p_plus()
              pscore = pscore_[0]
              s_plus()
              sscore = sscore_[0]
              move_one()
              output = questions[num[0]]['question']
              post_id = num[0]
              return {'output': output, 'post_id': post_id, 'pscore': pscore, 'sscore': sscore}
          elif post_id in choleric:
              p_plus()
              pscore = pscore_[0]
              c_plus()
              cscore = cscore_[0]
              move_one()
              output = questions[num[0]]['question']
              post_id = num[0]
              return {'output': output, 'post_id': post_id, 'pscore': pscore, 'cscore': cscore}
          else:
              p_plus()
              pscore = pscore_[0]
              move_one()
              output = questions[num[0]]['question']
              post_id = num[0]
              return {'output': output, 'post_id': post_id, 'pscore': pscore}

      elif post_id in choleric and request.method == "POST":
          if post_id in sanguine:
              c_plus()
              cscore = cscore_[0]
              s_plus()
              sscore = sscore_[0]
              move_one()
              output = questions[num[0]]['question']
              post_id = num[0]
              return {'output': output, 'post_id': post_id, 'cscore': cscore, 'sscore': sscore}
          else:
              c_plus()
              cscore = cscore_[0]
              move_one()
              output = questions[num[0]]['question']
              post_id = num[0]
              return {'output': output, 'post_id': post_id, 'cscore': cscore}

      elif post_id in sanguine and request.method== "POST":
          s_plus()
          sscore=sscore_[0]
          move_one()
          output = questions[num[0]]['question']
          post_id = num[0]
          return {'output': output, 'post_id': post_id, 'sscore': sscore}

      else:
          schore()
          score=score_[0]
          move_one()
          output = questions[num[0]]['question']
          post_id = num[0]
          return {'output': output, 'post_id': post_id, 'score':score}
      return render_template('index.html', onum=onum)

@app.route('/a', methods=['GET','POST'])
def indexa():
     onum=1
     if request.method == "POST":
        move_one()
        post_id=num[0]
        dato = dat()
        return dato
     return render_template('index.html', onum=onum)

def move_one():
    ques_int=num[0]
    new_num=ques_int+1
    num[0] = new_num

def schore():
    score_int = score_[0]
    new_score = score_int + 1
    score_[0] = new_score

def p_plus():
    score_int = pscore_[0]
    new_score = score_int + 1
    pscore_[0] = new_score

def c_plus():
    score_int = cscore_[0]
    new_score = score_int + 1
    cscore_[0] = new_score

def m_plus():
    score_int = mscore_[0]
    new_score = score_int + 1
    mscore_[0] = new_score

def s_plus():
    score_int = sscore_[0]
    new_score = score_int + 1
    sscore_[0] = new_score

def dat():
    firstname = questions[num[0]]['question']
    output = firstname
    post_id = num[0]
    score = score_[0]
    return {'output': output, 'post_id': post_id, 'score': score}


if __name__ == "__main__":
    app.run(debug=True)
