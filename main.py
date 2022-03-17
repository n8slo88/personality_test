from flask import Flask, render_template, url_for, request, jsonify
from flask_bootstrap import Bootstrap


#df = pandas.read_csv(r'templates/questionstwo.csv')
#questions = df.to_dict(orient="index")
questions={0: {'question': 'Click Agree to continue'}, 1: {'question': 'I react quickly when presented with an idea, a person, or a situation'}, 2: {'question': 'I react slowly when presented with an idea, a person, or a situation'}, 3: {'question': 'I react strongly (in intensity) when presented with an idea, a person, or a situation'}, 4: {'question': 'I do not react intensely when presented with an idea, a person, or a situation'}, 5: {'question': 'I want to take immediate action on an idea, in a situation, or with a person'}, 6: {'question': 'When presented with an idea, a person, or a situation, I remain calm and wait to react'}, 7: {'question': 'I do not react initially, but my reaction grows steadily in intensity'}, 8: {'question': 'Impressions last a long time'}, 9: {'question': 'Impressions last a short time (duration of reaction)'}, 10: {'question': 'Accepting'}, 11: {'question': 'Adventurous'}, 12: {'question': 'Worry Wart'}, 13: {'question': 'Introspective'}, 14: {'question': 'Easily provoked'}, 15: {'question': 'If provoked, will retaliate'}, 16: {'question': 'Serious'}, 17: {'question': 'Appreciate flattery'}, 18: {'question': 'Inclined to flatter'}, 19: {'question': 'Careful'}, 20: {'question': 'Inward'}, 21: {'question': 'Introverted'}, 22: {'question': 'Eye for detail'}, 23: {'question': 'Distractible'}, 24: {'question': 'Prone to reflection'}, 25: {'question': 'Determined'}, 26: {'question': 'Trusting'}, 27: {'question': 'Grudging'}, 28: {'question': 'Detached'}, 29: {'question': 'Love company'}, 30: {'question': 'Enjoy people'}, 31: {'question': 'Doubtful'}, 32: {'question': 'People-oriented'}, 33: {'question': 'Annoyed by disorder'}, 34: {'question': 'Abhor injustice'}, 35: {'question': 'Fair'}, 36: {'question': 'Easily angered'}, 37: {'question': 'Enthusiastic'}, 38: {'question': 'Extraverted'}, 39: {'question': 'Loner'}, 40: {'question': 'Skeptical'}, 41: {'question': 'Center of attention'}, 42: {'question': 'Revengeful'}, 43: {'question': 'Exaggerate easily'}, 44: {'question': 'Self-professed leader'}, 45: {'question': 'Servant-leader'}, 46: {'question': 'Charismatic'}, 47: {'question': 'Envious'}, 48: {'question': 'Jealous'}, 49: {'question': 'Happy'}, 50: {'question': 'Optimistic'}, 51: {'question': 'Prone to illness'}, 52: {'question': 'Easily discouraged'}, 53: {'question': 'Bullheaded'}, 54: {'question': 'Rational'}, 55: {'question': 'Diplomatic'}, 56: {'question': 'Tend to blurt things out'}, 57: {'question': 'Suspicious'}, 58: {'question': 'Peaceful'}, 59: {'question': 'Creative'}, 60: {'question': 'Take charge'}, 61: {'question': 'Patient'}, 62: {'question': 'Second-guessing'}, 63: {'question': 'Love peace and quiet'}, 64: {'question': 'Dutiful'}, 65: {'question': 'Hate conflict'}, 66: {'question': 'Love to debate'}, 67: {'question': 'Argumentative'}, 68: {'question': 'Sentimental'}, 69: {'question': 'Crowd-pleaser'}, 70: {'question': 'Slow to warm up'}, 71: {'question': 'Make friends easily'}, 72: {'question': 'Reticent'}, 73: {'question': 'Logical'}, 74: {'question': 'Pondering'}, 75: {'question': 'Love silence'}, 76: {'question': 'Fashionable'}, 77: {'question': 'Enjoy parties'}, 78: {'question': 'Prefer to be alone'}, 79: {'question': 'Artistic'}, 80: {'question': 'Poetic'}, 81: {'question': 'Thinker'}, 82: {'question': 'Talkative'}, 83: {'question': 'Abhor sentimentality'}, 84: {'question': 'Not empathetic'}, 85: {'question': 'Rule-oriented'}, 86: {'question': 'Persevering'}, 87: {'question': 'Flirtatious'}, 88: {'question': 'Reserved'}, 89: {'question': 'Easily slip into gossip'}, 90: {'question': 'Always right'}, 91: {'question': 'Looks are important'}, 92: {'question': 'Idea person'}, 93: {'question': 'Lack follow-through'}, 94: {'question': 'Love variety'}, 95: {'question': 'Affectionate'}, 96: {'question': 'Not affectively demonstrative'}, 97: {'question': 'Indifferent'}, 98: {'question': 'Wavering'}, 99: {'question': 'Hard to please'}, 100: {'question': 'Sober and practical'}, 101: {'question': 'Moody'}, 102: {'question': 'Composed'}, 103: {'question': 'Deliberate'}, 104: {'question': 'Prankster'}, 105: {'question': 'Obstinate'}, 106: {'question': 'Pessimistic'}, 107: {'question': 'Tolerant'}, 108: {'question': 'Courageous'}, 109: {'question': 'Timid'}, 110: {'question': '“Forgive and forget”'}, 111: {'question': '“Let’s wait and see”'}, 112: {'question': 'Hotheaded'}, 113: {'question': 'Prefer to follow'}, 114: {'question': 'Rash'}, 115: {'question': 'Intense'}, 116: {'question': 'Quick-tempered'}, 117: {'question': 'Frank'}, 118: {'question': 'Impatient'}, 119: {'question': 'Even-keeled'}, 120: {'question': 'Flighty'}, 121: {'question': 'Glass half-full'}, 122: {'question': 'Glass half-empty'}, 123: {'question': 'Bulldozer'}, 124: {'question': '“Strike while the iron is hot”'}, 125: {'question': 'Loose cannon'}, 126: {'question': 'Polite'}, 127: {'question': 'Easily aroused to debate'}, 128: {'question': 'Inwardly peaceful'}, 129: {'question': 'Good-natured'}, 130: {'question': 'Interruptive'}, 131: {'question': 'In tune with others’ feelings'}, 132: {'question': 'Strong-willed'}, 133: {'question': 'Contrary'}, 134: {'question': 'Fearless'}, 135: {'question': 'Ambitious'}, 136: {'question': 'Cheerful'}, 137: {'question': 'Self-composed'}, 138: {'question': 'Action-oriented'}, 139: {'question': 'Comfortable being a part of a group'}, 140: {'question': 'Prefer to take charge of a group'}, 141: {'question': 'Dislike groups'}, 142: {'question': 'Joiner'}, 143: {'question': 'Quick and decisive'}, 144: {'question': 'Robust'}, 145: {'question': 'Cordial'}, 146: {'question': 'Enjoy change'}, 147: {'question': 'Prefer routine'}, 148: {'question': 'Open and sociable'}, 149: {'question': 'Curious'}, 150: {'question': 'Critical'}, 151: {'question': 'Focus on problems'}, 152: {'question': 'Impulsive'}, 153: {'question': 'Methodical'}, 154: {'question': 'Bold'}, 155: {'question': 'Take initiative'}, 156: {'question': 'Insistent upon own plan'}, 157: {'question': 'Self-confident'}, 158: {'question': 'Self-reliant'}, 159: {'question': 'Sensitive'}, 160: {'question': 'Easily hurt'}, 161: {'question': 'Tendency to skim surface'}, 162: {'question': 'Adaptive'}, 163: {'question': 'Reclusive'}, 164: {'question': 'Self-conscious'}, 165: {'question': 'Overcautious'}, 166: {'question': 'Tends to discouragement'}, 167: {'question': 'Exclusive'}, 168: {'question': 'Private'}, 169: {'question': 'Mediator'}, 170: {'question': 'Indecisive'}, 171: {'question': 'Constant'}, 172: {'question': 'Competitive'}, 173: {'question': 'Self-sacrificing'}, 174: {'question': 'Respectful'}, 175: {'question': 'Adaptable'}, 176: {'question': 'Analytical'}, 177: {'question': 'Persistent'}, 178: {'question': 'Playful'}, 179: {'question': 'Laugh easily'}, 180: {'question': 'Spontaneous'}, 181: {'question': 'Hesitant'}, 182: {'question': 'Scheduled'}, 183: {'question': 'Outspoken'}, 184: {'question': 'Orderly'}, 185: {'question': 'Obliging'}, 186: {'question': 'Faithful'}, 187: {'question': 'Idealistic'}, 188: {'question': 'Inoffensive'}, 189: {'question': 'Dry wit'}, 190: {'question': 'Deep'}, 191: {'question': 'Mover'}, 192: {'question': 'Motivator'}, 193: {'question': 'Attentive to others'}, 194: {'question': 'Bossy'}, 195: {'question': 'Well-behaved'}, 196: {'question': 'Willful'}, 197: {'question': 'Perfectionist'}, 198: {'question': 'Peacekeeper'}, 199: {'question': 'Dispassionate'}, 200: {'question': 'Controlling'}, 201: {'question': 'Calm under fire'}, 202: {'question': 'Spiritual'}, 203: {'question': 'Love excitement'}, 204: {'question': 'Thoughtful'}, 205: {'question': 'Procrastinating'}, 206: {'question': 'Docile'}, 207: {'question': 'Headstrong'}, 208: {'question': 'Require rest'}, 209: {'question': 'Demand acknowledgment'}, 210: {'question': 'Need encouragement'}, 211: {'question': 'Need motivating'}, 212: {'question': 'Need friends'}, 213: {'question': 'Focused and intense'}, 214: {'question': 'Need fun'}, 215: {'question': 'Enjoy structure, procedures'}, 216: {'question': 'Need uplifting'}, 217: {'question': 'Non-confrontative'}, 218: {'question': 'Confrontative'}, 219: {'question': 'Pragmatic'}, 220: {'question': 'Mercurial'}, 221: {'question': 'Wary of new situations'}, 222: {'question': 'Singularly focused'}, 223: {'question': 'Like to shop and eat out'}, 224: {'question': 'Driven'}, 225: {'question': 'Will subjugate own desires to please others'}, 226: {'question': 'Process-oriented'}, 227: {'question': 'Goal-oriented'}, 228: {'question': 'Comfortable in present moment'}, 229: {'question': 'Future oriented'}, 230: {'question': 'A social butterfly'}, 231: {'question': 'Jokester'}, 232: {'question': 'Homebody'}, 233: {'question': 'END OF TEST'}}

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
     post_id=num[0]
     if request.method == "POST":
        move_one()
        output = questions[num[0]]['question']
        post_id = num[0]
        score=score_[0]
        return {'output': output, 'post_id': post_id, 'score': score}
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
