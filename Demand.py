import pandas as pd
print('\t\tWelcome To our Airport Management System ')
data1=pd.read_csv(r'new.csv')
data1.sort_values(["ORIGIN",'DEST'], axis = 0, ascending = [True,True], inplace = True, na_position ='last')
a=input("Enter The City From Where U Want To Start The Journey :")
b=input("Enter The City  Where U Want To End The Journey :")
if data1.loc[(data1['ORIGIN']==a)&(data1['DEST']==b)].sum==0:
      print("NO FLIGHTS AVAILABLE \t")
else:
  print("\tTHE HIGHEST NOS OF DEMAND IS FOR THE AILRLINES AT THE TOP OF THE LIST \t")
data1.sort_values(["PASSENGERS_ON_WAY"], axis = 0, ascending = [False], inplace = True, na_position ='last')
b=data1.loc[(data1['ORIGIN']==a)&(data1['DEST']==b)]
print(b.head())
print("THE AIRLINES WHICH IS IN MOST DEMAND AND ITS DETAILS ARE ")
print(b.head(1))
