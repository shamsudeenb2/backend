#MedicView
temp={}
            data=request.data
            if data.get('continues'):
                if data.get('times')=='daily':
                    if data.get('numbers')==1:
                        temp=findFrequency(1,data,med.id,'daily')
                    elif data.get('numbers')==2:
                        temp=findFrequency(2,data,med.id, 'daily')
                    elif data.get('numbers')==3:
                        temp=findFrequency(3,data,med.id, 'daily')
                    elif data.get('numbers')== 4:
                        temp=findFrequency(4,data,med.id,'daily')
                    elif data.get('numbers')==5:
                        temp=findFrequency(5,data,med.id, 'daily')
                elif data.get('times')=='hourly':
                    if data.get('numbers')==1:
                        temp=findFrequency(1,data,med.id,'hourly')
                    elif data.get('numbers')==2:
                        temp=findFrequency(2,data,med.id,'hourly')
                    elif data.get('numbers')==3:
                        temp=findFrequency(3,data,med.id,'hourly')
                    elif data.get('numbers')== 4:
                        temp=findFrequency(4,data,med.id,'hourly')
                    elif data.get('numbers')==5:
                        temp=findFrequency(5,data,med.id,'hourly')
                elif data.get('times')=='weekly':
                    if data.get('numbers')==1:
                        temp=findWeeklyFrequency(1,data,med.id)
                    elif data.get('numbers')==2:
                        temp=findWeeklyFrequency(2,data,med.id)
                    elif data.get('numbers')==3:
                        temp=findWeeklyFrequency(3,data,med.id)
                    elif data.get('numbers')== 4:
                        temp=findWeeklyFrequency(4,data,med.id)
                    elif data.get('numbers')==5:
                        temp=findWeeklyFrequency(5,data,med.id)
            else:
                temp['medics']=findDailyFrequency(1,data,med.id)
                
                
                
            serializer = FreqSerializer(data=temp, many=True)
            if serializer.is_valid():
                serializer.save()



# def findFrequency(n,data,id,tame):
    
    
#     
#     timeDiv=11//n
        
#     start=9
#     new_data=[]
#     medics={}
#     for x in range(n):
#         temp={}
        
#         time= "%s:%s:%s" % (start, 00, 00) if x==0 else "%s:%s:%s" % (addTime, 30, 00)
#         temp['medicine']= id
#         temp['date_to_take']= data.get('date_to_take')
#         temp['time_to_take']= time
#         temp['dose_to_take']= data.get('dose_to_take')
#         medics['medics']=temp
#         new_data.append(temp)
#         addTime=start + timeDiv
#         start = addTime
#     return new_data

# # def findHourlyFrequency(n,data,id):
# #     temp={}
# #     start=9
# #     new_data=[]
# #     for x in range(n):
# #         addTime=start + n
# #         time= "%s:%s:%s" % (start, 00, 00) if x==1 else "%s:%s:%s" % (addTime, 30, 00)
# #         temp['medicine']= id
# #         temp['date_to_take']= data.get('date_to_take')
# #         temp['time_to_take']= time
# #         temp['dose_to_take']= data.get('dose_to_take')
# #         new_data.append(temp)
    
# #     return new_data

# def findWeeklyFrequency(n,data,id):
#     temp={}
#     time=n/12
#     start=9
#     new_data=[]
#     for x in range(n):
#         addTime=start + time
#         time= "%s:%s:%s" % (start, 00, 00) if x==1 else "%s:%s:%s" % (addTime, 30, 00)
#         temp['medicine']= id
#         temp['date_to_take']= data.get('date_to_take')
#         temp['time_to_take']= time
#         temp['dose_to_take']= data.get('dose_to_take')
#         new_data.append(temp)
    
#     return new_data