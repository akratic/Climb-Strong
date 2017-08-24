# This is the most recent version of my project. I have a list of 5 workouts and function that calculates the 40 best weeks.

def score_this_week(week):
  c = {
  "climbing": { "fatigue": 4, "recovery": [2, 5, 8]},
  "hangboard": { "fatigue": 4, "recovery": [2, 5, 8]},
  "core": { "fatigue": 5, "recovery": [2, 3, 9] },
  "shoulders": { "fatigue": 3, "recovery": [2, 3, 6] },
  "rest": { "fatigue": 0, "recovery": [0, 1, 4] }
  }

  score = 0
  
  for index, item in enumerate(week):
    start = max(0, index - 2)
    relevant = week[start:index]
    count = relevant.count(item)
    # the recovery array feels upside down to me. I was expecting 14, 10, 6 not 6, 10, 14
    backwards = 2 - count
    delta = c[item]["recovery"][backwards] - c[item]["fatigue"]
    score += delta

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
