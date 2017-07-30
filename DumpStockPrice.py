import pandas
import pandas as pd
import Class

def fetch_attendance(year,SStockNumber,DStockDictionary):
	DataCsv = pandas.read_html("https://finance.google.com/finance/historical?cid=" + DStockDictionary[SStockNumber] + "&startdate=Jul%201%2C%202005&enddate=Jul%2029%2C%202017&num=200&ei=ePd7WYi4JMmz0ASxuL_4Cg&start=" + str(200*year))[2]
	DataCsv.columns = DataCsv.iloc[0]
	DataCsv['number'] = year*200
	return DataCsv[1:len(DataCsv)]




DStockDictionary = {2330:"674465", 2317:"674482", 6505:"686583", 2412:"677940", 3008:"683440", 2882:"674398"}
LStockList = [2330,2317,6505,2412,3008,2882]
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
