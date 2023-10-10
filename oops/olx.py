class Olx:
    vehicles=[      
            {"id":1,"name":"passionpro","year":2010,"selling_price":34000,"color":"black","location":"ekm"},  
            {"id":2,"name":"cbr","year":2011,"selling_price":128000,"color":"red","location":"tsr"},
            {"id":3,"name":"alto","year":2000,"selling_price":100000,"color":"silver","location":"tsr"},
            {"id":4,"name":"reclassic350","year":2018,"selling_price":120000,"color":"black","location":"ekm"},
            {"id":5,"name":"activa","year":2010,"selling_price":24000,"color":"black","location":"ekm"},
            {"id":6,"name":"herohondasd","year":2000,"selling_price":80000,"color":"red","location":"tsr"}        
                  
    ]

    def create(self,*args,**kwargs):
        self.vehicles.append(kwargs)
        print("vehicle added successfully")
        return kwargs
    def get(self,*args,**kwargs):
        return self.vehicles
    
    def retrieve(self,id=None,*args,**kwargs):
        obj=[veh for veh in self.vehicles if veh.get("id")==id][0]

        return obj
    
obj=Olx()  

print(obj.retrieve(id=2))
# print(obj.get())  
# print(obj.create(id=7,name="LAMBORGHINI",year=2022,selling_price=24000000,color="yellow",location="tvm"))