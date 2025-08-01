name = input("Enter your name: ")
age = int(input("Enter your age: "))
subject = input("Enter your favorite subject: ")
test_score = float(input("Enter your test score: "))

if test_score >= 75:
    print("Hello " + name + ", your favourite subject is " + subject +
          ". Your score is " + str(test_score) + ". Excellent work!")
elif 50 <= test_score < 74:
    print("Hello " + name + ", your favourite subject is " +
          subject + ". Your score is " + str(test_score) + ". Good!")
else:
    print("Hello " + name + ", your favourite subject is " + subject +
          ". Your score is " + str(test_score) + ". Needs Improvement!")
