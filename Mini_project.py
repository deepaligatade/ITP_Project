import streamlit as st
import pandas as pd
from PIL import Image
st.title("ITP Mini-Project")
show = st.sidebar.radio('Mini Project',['Problem Statement','Solution'])
d= {'Shipment_id': ['101','102','103','104','105','106'],
    'Sender':[1,4,2,1,3,5],
    'Receiver':[3,1,3,5,4,2],
    'Start Date':['14-03-2020','18-06-2020','1-12-2020','23-06-2020','29-08-2020','28-09-2020'],
    'Delivery Date':['25-03-2020','09-07-2020','Null','25-06-2020','10-09-2020','NULL'],
    'Sender Location':['Area1','Area2','Area5','Area1','Area5','Area3'],
    'Receiver Location':['Area6','Area4','Area1','Area4','Area3','Area1'],
    'Delivery Status':['Delivered','Delivered','In-Transit','Delivered','Delivered','In-Transit'],
    'Shipping Cost':[198,275,200,314,275,270] }
    #st.table(pd.DataFrame(d,columns=['Shipment id'	,'Sender',	'Receiver',	'Start date'	,'Delivery Date',	'sender_location'	,'Receiver_location',	'Delivery status'	,'Shipping cost']))
df_shipment = pd.DataFrame(d)
d1 = {'Client_id':[1,2,3,4,5],'Client Name':['Phillip','OmegaIII','Ramya','Romesh','John']}
df_client = pd.DataFrame(d1)
df_client=pd.DataFrame()
if show == 'Problem Statement':
    st.header('Problem Statement')
    st.write('For a seamless eCommerce shopping experience, it is essential to deliver the product promptly to the customer. And that’s where a professional courier service plays a vital role."Fastrack" courier company stores the relavant data of its clients and parcels in the form of dictionary. Create a dictionary for storing shipment information in key-value pairs. Shipment id is used as a key and list of other attributes like sender, receiver, start date,Delivery Date,sender_location,Receiver_location, Delivery status, Shipping cost is associated with shipment id. Use the data shown in the table below.')

    st.write(df_shipment)

    st.write(df_client)
if show=='Solution':
        st.write('Q1. Create a Dictionary of lists to store the information of shipments given in the table')
        sol= st.button('Show Solution',key=1)
        if sol:
            body = "ship = {101:[1, 3, '14-03-2020','25-03-2020','Area1','Area6','Delivered',198], 102: [4 ,1,'18-06-2020','09-07-2020','Area2','Area4','Delivered',275], 103 :[2,3,'01-12-2020','Null','Area5','Area1','In-Transit',200], 104 :[1,5,'23-06-2020','25-06-2020','Area1','Area4','Delivered',314], 105: [3,4,'29-08-2020','10-09-2020','Area5','Area3','Delivered',275], 106:[5,2,'28-09-2020','Null','Area3','Area1','In-Transit',270] } "
            st.code(body,language='python')
        st.write('Q2. Create a Dictionary of to store the information of clients given in the table.')
        sol1= st.button('Show Solution',key=2)
        if sol1:
            body = "clients = {1:'Phillip',2:'Omega III',3:'Ramya',4:'Romesh',5:'John'} "
            st.code(body,language='python')
        st.write('Q3. Write a code to replace clients id with their respective name in shipment dictionary using a loop and dictionary comprehension')
        hint = st.button('Show Hint',key=3)
        if hint:
            st.write('The original data for row 1: ')
            df = df_shipment.head(1)
            st.write(df)
            st.write('Sender and Receiver should be replaced as Phillip and Ramya respectively')
            st.write('Use loop / Dictionary Comprehension')
        sol2= st.button('Show Solution',key=4)
        if sol2:
            body = '''for i in ship:
                    a,b = ship[i][0],ship[i][1]
                    ship[i][0]=clients[a]
                    ship[i][1]=clients[b] '''
            st.code(body,language='python')
        sol2= st.button('Show alternate solution',key=5)
        if sol2:
            body = "ship1 = {i:[clients[ship[i][0]],clients[ship[i][1]],ship[i][2],ship[i][3],ship[i][4],ship[i][5],ship[i][6]] for i in ship} "
            st.code(body,language='python')
        
        st.write('Q4. Print all shipment details that are sent by Phillip')

        sol2= st.button('Show Solution',key=6)
        if sol2:
            body = '''for i in ship:
        if (ship[i][0] == 'Phillip'):
            print(ship[i]) '''
            st.code(body,language='python')
        st.write('Q5. Print all shipment details that are received by Ramya')

        sol2= st.button('Show Solution',key=7)
        if sol2:
            body = '''for i in ship:
    if (ship[i][1] == 'Ramya'):
        print(ship[i]) '''
            st.code(body,language='python')
        
        st.write('Q6. Print all shipments which are in "In-Transit" status')

        sol2= st.button('Show Solution',key=8)
        if sol2:
            body = ''' for i in ship:
    if (ship[i][6] == 'In-Transit'):
        print(ship[i]) '''
            st.code(body,language='python')
        
        st.write('Q7. Print all shipments which are delivered within 7 days of courier Start date')
        hint = st.button('Show Hint',key=9)
        if hint:
            st.write('Use Datetime library')
        sol2= st.button('Show Solution',key=10)
        if sol2:
            body = '''import datetime as dt
for i in ship:
    if (ship[i][3] != 'Null'):
        start = dt.datetime.strptime(ship[i][2], "%d-%m-%Y")
        end = dt.datetime.strptime(ship[i][3], "%d-%m-%Y")
        if (end-start)<= dt.timedelta(days=7):
            print(ship[i])
   '''
            st.code(body,language='python')
        
        st.write('Q8. Print all shipments which are delivered after 15 days of courier start date or not yet been delivered.')
        hint = st.button('Show Hint',key=11)
        if hint:
            st.write('Use Datetime library')
        sol2= st.button('Show Solution',key=12)
        if sol2:
            body = '''import datetime as dt
for i in ship:
    if (ship[i][3] == 'Null'):
        print(ship[i])
    else:
        start = dt.datetime.strptime(ship[i][2], "%d-%m-%Y")
        end = dt.datetime.strptime(ship[i][3], "%d-%m-%Y")
        if (end-start) > dt.timedelta(days = 15):
            print(ship[i]) '''
            st.code(body,language='python')

        st.write('Q9. Graph is used to represent networks of pickup and delivery area. Consider a below the graph diagram for given area locations in the table.')
        st.write('Sender location and receiver location is representated by node with area number.')
        st.write('Connection between two nodes shows route exists between those areas. E.g there exists a path from area 1 to area 2 but there is no direct route between area1 and area5.')
        st.write('Please note that this routes are bidirectional.')
        st.write('To reach to area5 from area1 , delivery person can take any route like 1-2-4-5 or 1-2-3-4-5¶')
      
        image = Image.open('graph.png')

        st.image(image, caption='A Connectivity Graph')
        st.write('Any graph like the one shown above can be represented by matrix shown below.')
        st.write('Presence of 1 represents the route between nodes and 0 represents there is no direct route exist between the nodes')
        image = Image.open('Matrix.png')
        st.image(image, caption='adjacency matrix')
        st.write('Write a function find_all_routes to display all possible routes from senders location to receivers location given in the dictionary for each shipment.')

        hint = st.button('Show Hint',key=16)
        if hint:
            st.write('The adjacency matrix can be stored as nested list.')
            st.write('Finding all routes can be written as recursive function ')
        sol2= st.button('Show Solution',key=17)
        if sol2:
            st.write('Recursive Function for route finding')
            body = '''def find_all_routes(matrix,u,d,visited,path):     
        visited[u]= True
        path.append(u+1) 
        if u == d: 
            print(path) 
        else: 
             
            for i in range(6):
                if matrix[u][i] == 1 and (visited[i]== False): 
                    find_all_routes(matrix,i, d, visited, path) 
                    ## for j in range(6):
                            if matrix[i][j] 
       
        path.pop() ## Dealing with dead ends
        visited[u]= False '''
            st.code(body,language='python')
            st.write('Creation of adjacency matrix and initialisation of data')
            body = '''matrix = [[0,1,0,0,0,1],[1,0,1,1,0,0],[0,1,0,1,0,0],[0,1,1,0,1,0],[0,0,0,1,0,0],[1,0,0,0,0,0]] ## Nested list
visited=[False for i in range(6)]
path = []'''
            st.code(body,language='python')
            st.write('Calling the recrsive function for all sender and receiver')
            body = '''def Show_all(ship):
    for i in ship:
        print('Shipment Id: ',i)
        s = int(ship[i][4][-1])
        print("Sender's Location" , s)
        r = int(ship[i][5][-1])
        print("Receiver's Location" , r)
        print('All possible routes : ')
        find_all_routes(matrix,s-1,r-1,visited,path)
        print('-----------------------------------')
        
Show_all(ship)'''
            st.code(body,language ='python')
