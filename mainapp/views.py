from django.shortcuts import render,redirect
from django.contrib import messages
# Create your views here.

def home(request):
    #print(count)
    return render(request,'home.html')



def hegit_weight_to_bmi(height,weight):
    height = height * 0.3048
    bmi=round(weight/(height*height),2)
    if (bmi < 16):
        return 0
    elif (bmi < 18.5):
        return 1
    elif (bmi < 25):
        return 2
    elif (bmi < 30):
        return 3
    elif (bmi < 35):
        return 4
    elif (bmi >= 35):
        return 5
    return 0


def age_to_score(age):
    if (age< 30):
        return 0
    elif (age< 40):
        return 1
    elif (age < 50):
        return 2
    elif (age < 60):
        return 3
    elif (age < 70):
        return 4
    elif (age >= 70):
        return 5
    return 0


def heart_score(sex,age,systolic,diastolic,heartRate, hdl,ldl,totalCho,diabetes,height,weight,smoker):
    bmi=hegit_weight_to_bmi(height,weight)
    age=age_to_score(age)

    sexScor=(0.317, 0.169)
    ageScor=(0.02, 0.04, 0.061, 0.153, 0.276, 0.407)
    systolicScor=(0.113, 0.169, 0.194, 0.305, 0.411)
    diastolicScor=(0.216, 0.219, 0.317, 0.333)
    heartRateScor=(0.221, 0.246, 0.3, 0.333, 0.5)
    ldlScor=(0.206, 0.221, 0.228, 0.23, 0.258)
    hdlScor=(0.363, 0.228, 0.163)
    totalChoScor=(0.226, 0.228, 0.239)
    diabetesScor=(0.212, 0.481)
    bmiScor=(0.143, 0.211, 0.238, 0.25, 0.269, 0.366)
    smokerScor=(0.107, 0.228, 0.233, 0.243, 0.25, 0.274)
    totalScor=sexScor[sex]+ageScor[age]+systolicScor[systolic]+diastolicScor[diastolic]+heartRateScor[heartRate]
    totalScor=totalScor+ldlScor[ldl]+hdlScor[hdl]+totalChoScor[totalCho]+ diabetesScor[diabetes]+ bmiScor[bmi]+smokerScor[smoker]
    cvd=totalScor/11
    return totalScor,cvd



def submitPage(request):
    if request.method == 'POST':
        if (request.POST['age'] =="") or (request.POST['height'] =="") or (request.POST['weight'] ==""):
            messages.info(request,'No field can remain blank!')
            return redirect('submitPage')

        sex = int(request.POST['sex'])
        age = int(request.POST['age'])
        systolic = int(request.POST['systolic'])
        diastolic = int(request.POST['diastolic'])
        heartRate = int(request.POST['heartRate'])
        hdl = int(request.POST['hdl'])
        ldl = int(request.POST['ldl'])
        totalCho = int(request.POST['totalCho'])
        diabetes = int(request.POST['diabetes'])
        height = float(request.POST['height'])
        weight = float(request.POST['weight'])
        smoker = int(request.POST['smoker'])


        totalScor,cvd=heart_score(sex,age,systolic,diastolic,heartRate, hdl,ldl,totalCho,diabetes,height,weight,smoker)
        #print(totalScor+" "+cvd)
        return render(request,'resultPage.html',{"totalScor":totalScor,"cvd":cvd})
    else:
        return render(request,'submitPage.html')
