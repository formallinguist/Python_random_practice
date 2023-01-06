# 5.3 London's weather
import pandas as pd 

def londons_weather(temperature, input, outputfile):
    df1 = pd.read_csv(input,sep="\t")
    cols=["Year","Month","Day"]
    #df_data['date'] = df1[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")
    df_data = df1[["Temperature","Precipitation","Wind-speed"]][df1["Temperature"]>float(temperature)]
    cols=["Year","Month","Day"]
    df_data['date'] = df1[cols].apply(lambda x: '-'.join(x.values.astype(str)), axis="columns")
    df_data = df_data[["date","Temperature","Precipitation","Wind-speed"]]
    df_data.to_csv(outputfile)
    length = len(df_data)
    average ="{:.2f}".format(df_data["Temperature"].sum()/length)
    total__preci = "{:.2f}".format(df_data["Precipitation"].sum())
    average_win = "{:.2f}".format(df_data["Wind-speed"].sum()/length)

    return "Total entries: " + str(length) + "\nAverage temperature:" + average + '\nTotal precipitation:'+ total__preci+'\nAverage wind-speed:'+ average_win

temp_input = input("Enter temperature")
print(londons_weather(temp_input,"weather.csv","output.csv"))
