# In this version I added two exceptions. 
#The first ValueError is raised when a week has more or fewer days than 7.
# The second ValueError is raised when a given workout is not in "c". 

def score_this_week(week):
  c = {
  "climbing": { "fatigue": 4, "recovery": [2, 5, 8]},
  "hangboard": { "fatigue": 4, "recovery": [2, 5, 8]},
  "core": { "fatigue": 5, "recovery": [2, 3, 9] },
  "shoulders": { "fatigue": 3, "recovery": [2, 3, 6] },
  "rest": { "fatigue": 0, "recovery": [0, 1, 4] }
  }

  score = 0
  past_days = []


  for index, item in enumerate(week):
    if len(week) != 7:
        raise ValueError("Week {} has {} days!".format(week, len(week)))
    if index-1 < 0: 
      past_days.append([None, None].count(item))
    elif index-2 < 0:
  	  past_days.append([None, week[index-1]].count(item)) 
    else:
      past_days.append([week[index-2], week[index-1]].count(item))

  for workout, past_value in zip(week, past_days):
    if workout not in c:
        raise ValueError("({}) is not a workout".format(workout))     
    elif past_value == 0:
        score += c[workout]["recovery"][2] - c[workout]["fatigue"]
    elif past_value == 1:
        score += c[workout]["recovery"][1] - c[workout]["fatigue"]
    else:
        score += c[workout]["recovery"][0] - c[workout]["fatigue"]
  return score

def main():
  import itertools

  workouts = ["climbing", "hangboard", "core", "rest", "shoulders"]

  def cartesian_product(iterables):
    return list(itertools.product(iterables, repeat=7))

  weeks = cartesian_product(workouts)
  
  all_scores = []
  for index, week in enumerate(weeks):
    all_scores.append(score_this_week(week))

  all_weeks = []
  for week in (weeks):
    all_weeks.append(week)
  

  def sort_weeks_and_scores(all_scores, all_weeks):
    return week[0]

  print sorted(zip(all_scores, all_weeks))[-40:]


#print sorted(student_tuples, key=lambda student: student[2])

#def sort_key(student):
    #return student[2]

#print sorted(student_tuples, key=sort_key)

  #print sorted(zip(all_scores, all_weeks), key=lambda week: week[0])[-40:]

  #print "The best week is {}. Score: {}".format(weeks[all_scores.index(max(all_scores))], max(all_scores))
  #print "The worst week is {}. Score: {}".format(weeks[all_scores.index(min(all_scores))], min(all_scores))

  """for index, week in enumerate(weeks):
        print "Week {} = {} <> {}".format(index+1, score_this_week(week), week)"""

if  __name__ =='__main__':
  main()