class quiz():
	questions=[]#add questions here
	answers=[]#add corisponding answers here
	points=0
	name=None
	wrong=[]
	def ask_a_question(index):
		userin=input(quiz.questions[index])
		if userin.lower()==quiz.answers[index]:
			quiz.points+=1
		else:
			quiz.wrong.append(quiz.questions[index])
	def run():
		quiz.name=input("what is thy name: ")
		for i in enumerate(quiz.questions):
			quiz.ask_a_question(i[0])
			
		print(f"you got {quiz.points} correct, your score is {quiz.points/len(quiz.questions)*100}")
		score_report.save()
class score_report():
	def save():
		attempt=1
		if (quiz.points/len(quiz.questions))*100>69:
			passed='passed'
		else:
			passed = 'not passed'
		while True:
			try:
				open(f"report-{attempt}.txt",'x')
				break
			except:
				attempt+=1
		with open(f"report-{attempt}.txt",'w') as file:
			file.write(f"{quiz.name}\nyou got {(quiz.points/len(quiz.questions))*100}%\nyou got {quiz.points}/{len(quiz.questions)}\nyou {passed}\n")
		with open(f"report-{attempt}.txt",'a') as file:
			for i in quiz.wrong:
				file.write(f"you got {i} wrong the answer was {quiz.answers[quiz.questions.index(i)]}\n")
quiz.run()
