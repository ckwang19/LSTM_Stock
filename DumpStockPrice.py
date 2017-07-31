import pandas
import pandas as pd
import Class

def fetch_attendance(year,SStockNumber,DStockDictionary):
	DataCsv = pandas.read_html("https://finance.google.com/finance/historical?cid=" + DStockDictionary[SStockNumber] + "&startdate=Jul%201%2C%202005&enddate=Jul%2029%2C%202017&num=200&ei=ePd7WYi4JMmz0ASxuL_4Cg&start=" + str(200*year))[2]
	DataCsv.columns = DataCsv.iloc[0]
	DataCsv['number'] = year*200
	return DataCsv[1:len(DataCsv)]

#https://finance.google.com/finance/historical?cid=674465&startdate=Jul%201%2C%202005&enddate=Jul%2029%2C%202017&num=200&ei=ePd7WYi4JMmz0ASxuL_4Cg&start=200


DStockDictionary = {2330:"674465", 2317:"674482",	6505:"686583", 	2412:"677940", 3008:"683440", \
					2882:"674398", 1303:"671742",	1301:"674479", 	1326:"684596", 2881:"684599", \
					2454:"683538", 2308:"674459",	2002:"674402", 	2891:"683792", 3045:"672195", \
					2886:"674413", 2311:"675428",	1216:"678170", 	2382:"671746", 2474:"683442", \
					2912:"671745", 4938:"14571124", 2892:"684593", 	4904:"680861", 2357:"674388", \
					2207:"683612", 2105:"679212",	5880:"11801887",2880:"683803", 2884:"684083", \
					2303:"681098", 2408:"671751",	2395:"683127", 	2801:"674399", 2885:"684627", \
					2325:"674464", 3481:"706080",	2883:"683780", 	2887:"672259", 1402:"674471", \
					1101:"671639", 2354:"687970", 	9904:"683301", 	2409:"675616", 2301:"674439", \
					2823:"687820", 8464:"624644977211532", 2890:"682750", 5871:"658368721561093",\
					6456:"530366484279123"}
LStockList = [2330,2317,6505,2412,3008,2882,1303,1301,1326,2881,2454,2308,2002,2891,3045,2886,2311,1216, \
			  2382,2474,2912,4938,2892,4904,2357,2207,2105,5880,2880,2884,2303,2408,2395,2801,2885,2325, \
			  3481,2883,2887,1402,1101,2354,9904,2409,2301,2823,8464,2890,5871,6456]
for SStockNumber in LStockList:
	FStock = open('StockData/' + str(SStockNumber), 'a')
	DataCsv = pd.concat(fetch_attendance(year,SStockNumber,DStockDictionary) for year in range(0, 14))
	#print len(DataCsv)
	for NDataCounter in range(len(DataCsv)):
		OStock = Class.Stock(DataCsv[NDataCounter:1+NDataCounter]['Date'].values.tolist()[0], DataCsv[NDataCounter:1+NDataCounter]['Open'].values.tolist()[0], DataCsv[NDataCounter:1+NDataCounter]['High'].values.tolist()[0], DataCsv[NDataCounter:1+NDataCounter]['Low'].values.tolist()[0], DataCsv[NDataCounter:1+NDataCounter]['Close'].values.tolist()[0], DataCsv[NDataCounter:1+NDataCounter]['Volume'].values.tolist()[0])
		LObjList = []
		LObjList.append(OStock.m_Date)
		LObjList.append(OStock.m_Open)
		LObjList.append(OStock.m_High)
		LObjList.append(OStock.m_Low)
		LObjList.append(OStock.m_Close)
		LObjList.append(OStock.m_Volume)
		FStock.write("\t".join(LObjList))
		FStock.write("\n")
		del LObjList
		#print DataCsv[0:1]['Open'].values.tolist()
		#print DataCsv[0:1]['Open'].values.tolist()[0]
	FStock.close()
