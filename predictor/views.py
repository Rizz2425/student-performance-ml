from django.shortcuts import render
import pickle
import pandas as pd

with open('student_model.pkl', 'rb') as f:
    model = pickle.load(f)

def home(request):
    result = None
    if request.method == 'POST':
        
        study_hours = float(request.POST.get('study_hours'))
        attendance = float(request.POST.get('attendance'))
        prev_score = float(request.POST.get('prev_score'))

        
        input_data = pd.DataFrame([[study_hours, attendance, prev_score]], 
                                 columns=['Study_Hours', 'Attendance', 'Previous_Score'])

        
        prediction = model.predict(input_data)
        
        if prediction[0] == 1:
            result = "Pass (Congratulations!)"
        else:
            result = "Fail (Needs Improvement)"

    return render(request, 'index.html', {'result': result})