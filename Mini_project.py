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
        sol= st.button('Show Hint',key=1)
        if sol:
            st.write("Dictionary can be created using id as key and list of other data as value")
            st.write("The first row can be created as follows")
            st.write("ship = {101:[1, 3, '14-03-2020','25-03-2020','Area1','Area6','Delivered',198],key2:[values for row 2] .......")
            #st.code(body,language='python')
        st.write('Q2. Create a Dictionary of to store the information of clients given in the table.')
        sol1= st.button('Show Hint',key=2)
        if sol1:
            st.write("Create the dictionary with key as client_id and value as Client Name")
            st.write('dict_client = {client_id1:client_name1,client_id2:client_name2......}')
        st.write('Q3. Write a code to replace clients id with their respective name in shipment dictionary using a loop and dictionary comprehension')
        hint = st.button('Show Hint',key=3)
        if hint:
            st.write('The original data for row 1: ')
            df = df_shipment.head(1)
            st.write(df)
            st.write('Sender and Receiver should be replaced as Phillip and Ramya respectively')
            st.write('Use loop / Dictionary Comprehension')
        
        
        st.write('Q4. Print all shipment details that are sent by Phillip')

        sol2= st.button('Show Hint',key=6)
        if sol2:
            st.write("Use the modified dictionary of Question 3")
            st.write("Use loops to check Phillip in the sender data")
            st.write("The expected output is")
            st.write("['Phillip', 'Ramya', '14-03-2020', '25-03-2020', 'Area1', 'Area6', 'Delivered']",
"['Phillip', 'John', '23-06-2020', '25-06-2020', 'Area1', 'Area4', 'Delivered']",sep = '\n')
        st.write('Q5. Print all shipment details that are received by Ramya')

        sol2= st.button('Show Hint',key=7)
        if sol2:
            st.write("Use the modified dictionary of Question 3")
            st.write("Use loops to check Ramya in the receiver data")
            st.write("The expected output is")
            st.write("['Phillip', 'Ramya', '14-03-2020', '25-03-2020', 'Area1', 'Area6', 'Delivered']",
 "['Omega III', 'Ramya', '01-12-2020', 'Null', 'Area5', 'Area1', 'In-Transit']",sep='\n')
        
        st.write('Q6. Print all shipments which are in "In-Transit" status')

        sol2= st.button('Show Hint',key=8)
        if sol2:
            st.write("Use the modified dictionary of Question 3")
            st.write("Use loops to check 'In Transit' in the status")
            st.write("The expected output is")
            st.write("['Omega III', 'Ramya', '01-12-2020', 'Null', 'Area5', 'Area1', 'In-Transit']",
"['John', 'Omega III', '28-09-2020', 'Null', 'Area3', 'Area1', 'In-Transit']",sep='\n')
        
        st.write('Q7. Print all shipments which are delivered within 7 days of courier Start date')
        hint = st.button('Show Hint',key=9)
        if hint:
            st.write('Use Datetime library')
            st.write("Convert the date related data i.e. 'start date' and 'delivery date' to date data type")
            st.write("Use timedelta for calculating date difference")
        
        st.write('Q8. Print all shipments which are delivered after 15 days of courier start date or not yet been delivered.')
        hint = st.button('Show Hint',key=11)
        if hint:
            st.write('Use Datetime library')
            st.write("Convert the date related data i.e. 'start date' and 'delivery date' to date data type")
            st.write("Use timedelta for calculating date difference")
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
            st.write('Keep track of places that are already visited to confirm that no place is visited repeatedly')
            st.write('Use appropriate Graph traversal method to find the paths')
        graphs =st.button("More about Graphs",key=17)
        if graphs:
            st.write(' Graphs are mathematical concepts that have found many uses in computer science. Graphs come in many different flavors, many of which have found uses in computer programs. ')
            st.write('Some flavors are: Simple graph, Undirected or directed graphs, Cyclic or acyclic graphs, labeled graphs, Weighted graphs, Infinite graphs, ... and many more too numerous to mention.')
            #st.write('Most graphs are defined as a slight alteration of the following rules. A graph is made up of two sets called Vertices and Edges.')
            st.write('The Vertices are drawn from some underlying type, and the set may be finite or infinite. Each element of the Edge set is a pair consisting of two elements from the Vertices set.')
            st.write('Graphs are often depicted visually, by drawing the elements of the Vertices set as boxes or circles, and drawing the elements of the edge set as lines or arcs between the boxes or circles.')
            st.write(' There is an arc between v1 and v2 if (v1,v2) is an element of the Edge set. Adjacency: If (u,v) is in the edge set we say u is adjacent to v (which we sometimes write as u ~ v).')
                              
