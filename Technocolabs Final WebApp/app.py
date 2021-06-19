from flask import Flask, request, render_template
from flask_cors import CORS
import sklearn
import pickle
import pandas as pd

app = Flask(__name__)
CORS(app)
model = pickle.load(open("flight_rf.pkl", "rb"))

@app.route("/")
#@cross_origin()

def home():
    return render_template("home.html")


@app.route("/predict", methods = ["GET", "POST"])
#CORS(app)
#@cross_origin()
def predict():
    if request.method == "POST":

        # Date_of_Journey
        date_dep = request.form["Dep_Time"]
        Out_Day = int(pd.to_datetime(date_dep, format="%Y-%m-%dT%H:%M").day)
        Out_Month = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").month)
        # print("Journey Date : ",Journey_day, Journey_month)

        # Departure
        Dep_hour = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").hour)
        Dep_min = int(pd.to_datetime(date_dep, format ="%Y-%m-%dT%H:%M").minute)
        # print("Departure : ",Dep_hour, Dep_min)

        # Arrival
        date_arr = request.form["Arrival_Time"]
        Arrival_hour = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").hour)
        Arrival_min = int(pd.to_datetime(date_arr, format ="%Y-%m-%dT%H:%M").minute)
        # print("Arrival : ", Arrival_hour, Arrival_min)

        # Duration
        Duration_Hours = abs(Arrival_hour - Dep_hour)
        Duration_Mins = abs(Arrival_min - Dep_min)
        # print("Duration : ", dur_hour, dur_min)


        # Total Stops
        Total_Stops = int(request.form["Total_Stops"])
        # print(Total_stops)


        # Airline
        # Air India = 0 (not in column)
        Out_Airline = request.form['Out_Airline']
        if(Out_Airline=='AirAsia_India'):
            IndiGo = 0
            AirAsia_India = 1
            Multiple_Airlines = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        elif(Out_Airline=='IndiGo'):
            IndiGo = 1
            AirAsia_India = 0
            Multiple_Airlines = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        elif(Out_Airline=='Multiple Airlines'):
            IndiGo = 0
            AirAsia_India = 0
            Multiple_Airlines = 1
            SpiceJet = 0
            Vistara = 0
            GoAir = 0

        elif(Out_Airline=='SpiceJet'):
            IndiGo = 0
            AirAsia_India = 0
            Multiple_Airlines = 0
            SpiceJet = 1
            Vistara = 0
            GoAir = 0

        elif(Out_Airline=='Vistara'):
            IndiGo = 0
            AirAsia_India = 0
            Multiple_Airlines = 0
            SpiceJet = 0
            Vistara = 1
            GoAir = 0

        elif(Out_Airline=='GoAir'):
            IndiGo = 0
            AirAsia_India = 0
            Multiple_Airlines = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 1

        else:
            IndiGo = 0
            AirAsia_India = 0
            Multiple_Airlines = 0
            SpiceJet = 0
            Vistara = 0
            GoAir = 0


        # Out_Cities
        # Ahmedabad = 0 (not in column) AMD
        Source = request.form["Out_Cities"]    ##"Out_Cities"
        if (Source == 'Bengaluru'):
            Out_Cities_BLR = 1
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

        elif (Source == 'Mumbai'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 1
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0


        elif (Source == 'Kozhikode'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 1
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0


        elif (Source == 'Kolkata'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 1
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

        elif (Source == 'Kannur'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 1
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

        elif (Source == 'Delhi'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 1
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

        elif (Source == 'Guwahati'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 1
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

        elif (Source == 'Leh'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 1
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

        elif (Source == 'Ranchi'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 1
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

        elif (Source == 'Jaipur'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 1
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

        elif (Source == 'Chennai'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 1
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

        elif (Source == 'Shillong'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 1
            Out_Cities_VNS = 0

        elif (Source == 'Varanasi'):
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 1

        else:
            Out_Cities_BLR = 0
            Out_Cities_BOM = 0
            Out_Cities_CCJ = 0
            Out_Cities_CCU = 0
            Out_Cities_CNN = 0
            Out_Cities_DEL = 0
            Out_Cities_GAU = 0
            Out_Cities_IXL = 0
            Out_Cities_IXR = 0
            Out_Cities_JAI = 0
            Out_Cities_MAA = 0
            Out_Cities_SHL = 0
            Out_Cities_VNS = 0

    #Destination begins now.

        # Agatti Island [AGX] = 0 (not in column)
        destination = request.form["Return_Cities"]   ##"Return_Cities"
        if (destination == 'Ahmedabad'):
            Return_Cities_AMD = 1
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Amritsar'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 1
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Bengaluru'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 1
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Coimbatore'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 1
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Delhi'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 1
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Guwahati'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 1
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Gorakhpur'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 1
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Hyderabad'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 1
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Mangalore'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 1
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Lucknow'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 1
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Chennai'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 1
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Patna'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 1
            Return_Cities_STV = 0
            Return_Cities_VGA = 0

        elif (destination == 'Surat'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 1
            Return_Cities_VGA = 0

        elif (destination == 'Vijaywada'):
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 1

        else:
            Return_Cities_AMD = 0
            Return_Cities_ATQ = 0
            Return_Cities_BLR = 0
            Return_Cities_CJB = 0
            Return_Cities_DEL = 0
            Return_Cities_GAU = 0
            Return_Cities_GOP = 0
            Return_Cities_HYD = 0
            Return_Cities_IXE = 0
            Return_Cities_LKO = 0
            Return_Cities_MAA = 0
            Return_Cities_PAT = 0
            Return_Cities_STV = 0
            Return_Cities_VGA = 0


    ##PREDICTION

        prediction = model.predict([[
            	Out_Day,
                Out_Month,
                Duration_Hours,
                Duration_Mins,
                Dep_hour,
                Dep_min,
                Arrival_hour,
                Arrival_min,
                Total_Stops,
                AirAsia_India,
                GoAir,
                IndiGo,
                Multiple_Airlines,
                SpiceJet,
                Vistara,
                Out_Cities_BLR,
                Out_Cities_BOM,
                Out_Cities_CCJ,
                Out_Cities_CCU,
                Out_Cities_CNN,
                Out_Cities_DEL,
                Out_Cities_GAU,
                Out_Cities_IXL,
                Out_Cities_IXR,
                Out_Cities_JAI,
                Out_Cities_MAA,
                Out_Cities_SHL,
                Out_Cities_VNS,
                Return_Cities_AMD,
                Return_Cities_ATQ,
                Return_Cities_BLR,
                Return_Cities_CJB,
                Return_Cities_DEL,
                Return_Cities_GAU,
                Return_Cities_GOP,
                Return_Cities_HYD,
                Return_Cities_IXE,
                Return_Cities_LKO,
                Return_Cities_MAA,
                Return_Cities_PAT,
                Return_Cities_STV,
                Return_Cities_VGA,
            ]])

        output=round(prediction[0],2)

        return render_template('home.html',prediction_text="Your Flight price from {} to {} is Rs. {}".format(Source, destination, output))


    return render_template("home.html")




if __name__ == "__main__":
    app.run(debug=True)
