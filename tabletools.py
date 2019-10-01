# tabletools.py

class LabeledList():
    def __init__(self, data=None, index=None):
        self.values = data
        if index is None:
            self.values = data
            self.index = list(range(0,len(self.values)))
            
        elif index is not None:
            self.index = index
        
    def __str__(self):
        string = ""
        if len(self.values) == 0:
            return string
        if isinstance(self.values[0], str):
            len_data = len(max(self.values, key=len))
        elif isinstance(self.values[0], int) or isinstance(self.values[0], float):
            len_data = len(str(max(self.values)))
        else :
            len_data = 5

        if isinstance(self.index[0], str):
            len_index = len(max(self.index, key=len))
        elif isinstance(self.index[0], int) or isinstance(self.index[0], float):
            len_index = len(str(max(self.index)))
        else :
            len_index = 5
            
        format_spec_d=f'>{len_data}'
        format_spec_i=f'>{len_index}'
        for i, d in zip(self.index, self.values):
            string = string + f'{str(i):{format_spec_i}}' + " " + f'{str(d):{format_spec_d}}' + '\n'
        string = string[:-1]
        return string

    def __repr__(self):
        return "LabledList(index = %s, data = %s)"%(str(self.index),str(self.values))

    def __getitem__(self, key_list):
        newIndex=[]
        newData=[]
        
        if isinstance(key_list, LabeledList):
            for i,d in zip(self.index, self.values):
                if i in key_list.values:
                    newIndex.append(i)
                    newData.append(d)
            newLL = LabeledList(newData,newIndex)
            return newLL
            
        elif isinstance(key_list, list):
            if isinstance(key_list[0], bool):
                indexT = [i for i, x in enumerate(key_list) if x is True]
                for it in indexT:
                    newIndex.append(self.index[it])
                    newData.append(self.values[it])
                newLL = LabeledList(newData,newIndex)
                return newLL
            else:
                for i,d in zip(self.index,self.values):
                    if i in key_list:
                        newIndex.append(i)
                        newData.append(d)
                newLL = LabeledList(newData,newIndex)
                return newLL
            
        elif isinstance(key_list, int) or isinstance(key_list, float) or isinstance(key_list, str) or isinstance(key_list, bool):
            for i,d in zip(self.index,self.values):
                if i == key_list:
                    newData.append(d)
                    newIndex.append(i)
            if len(newIndex)==1:
                newLL = newData[0]
            else:
                newLL = LabeledList(newData,newIndex)
            return newLL

    def __iter__(self):
        return iter(self.values)

##    def __next__(self):
##        count = 0
##        if count == len(self.index):
##            raise StopIteration
##        else:
##            count = count + 1
##            return self.data[count]
    
    def __eq__(self, scalar):
        newData = [True if d == scalar else False for d in self.values ]
        newLL = LabeledList(newData, self.index)
        return newLL

    def __ne__(self, scalar):
        newData = [True if d != scalar else False for d in self.values ]
        newLL = LabeledList(newData, self.index)
        return newLL

    def __gt__(self, scalar):
        newData = [True if d > scalar else False for d in self.values ]
        newLL = LabeledList(newData, self.index)
        return newLL

    def __lt__(self, scalar):
        newData = [True if d < scalar else False for d in self.values ]
        newLL = LabeledList(newData, self.index)
        return newLL    

    def map(self, f):
        newData=[]
        for d in self.values:
            newData.append(f(d))
        newLL = LabeledList(newData, self.index)
        return newLL

class Table():
    def __init__(self, data, index=None, columns=None):
        self.values = data
        len_data = len(max(self.values, key=len))
        if index == None and columns == None:
            self.index = list(range(0,len(self.values)))
            self.columns = list(range(0,len_data))
        elif columns == None:
            self.columns = list(range(0,len_data))
            self.index=index
        elif index == None:
            self.index = list(range(0,len(self.values)))
            self.columns=columns
        else:
            self.columns=columns
            self.index=index

    def __str__ (self):
        len_data = 0
        len_index = 0
        count_data = 0
        string = "" 

        if isinstance(self.index[0], str):
            len_index = len(max(self.index, key=len))
        elif isinstance(self.index[0], int) or isinstance(self.index[0], float):
            len_index = len(str(max(self.index)))
        else :
            len_index = 5

        len_col=[]
        for i in range(len(self.columns)):
            len_col.append(len(str(self.columns[i])))

        count_len = 0
        for i in range(len(self.columns)):
            for d in self.values:
                for di in d:
                    len_data = len(str(d[count_len]))
                    
                    if len_col[count_len]<len_data:
                        len_col[count_len]=len_data
                    count_len= count_len+1
                count_len=0
        count_len = 0
        
        format_spec_i=f'>{len_index}'
        tempColumns = self.columns
        string = string + f'{"":{format_spec_i}}' + " "
        for c in tempColumns:
            format_spec_d=f'>{len_col[count_len]}'
            string = string + f'{str(c):{format_spec_d}}' + " "
            count_len = count_len + 1
        count_len = 0
        string = string + '\n'
        for i in self.index:
            string = string + f'{str(i):{format_spec_i}}' + " "
            for d in self.values[count_data]:
                format_spec_d=f'>{len_col[count_len]}'
                string = string + f'{str(d):{format_spec_d}}' + " "
                count_len = count_len + 1
            count_len = 0
            count_data=count_data+1
            string = string + '\n'
        string = string[:-1]
        return string
        
    def __repr__ (self):
        len_data = 0
        len_index = 0
        count_data = 0
        string = "" 

        if isinstance(self.index[0], str):
            len_index = len(max(self.index, key=len))
        elif isinstance(self.index[0], int) or isinstance(self.index[0], float):
            len_index = len(str(max(self.index)))
        else :
            len_index = 5

        len_col=[]
        for i in range(len(self.columns)):
            len_col.append(len(str(self.columns[i])))

        count_len = 0
        for i in range(len(self.columns)):
            for d in self.values:
                for di in d:
                    len_data = len(str(d[count_len]))
                    
                    if len_col[count_len]<len_data:
                        len_col[count_len]=len_data
                    count_len= count_len+1
                count_len=0
        count_len = 0
        
        format_spec_i=f'>{len_index}'
        tempColumns = self.columns
        string = string + f'{"":{format_spec_i}}' + " "
        for c in tempColumns:
            format_spec_d=f'>{len_col[count_len]}'
            string = string + f'{str(c):{format_spec_d}}' + " "
            count_len = count_len + 1
        count_len = 0
        string = string + '\n'
        for i in self.index:
            string = string + f'{str(i):{format_spec_i}}' + " "
            for d in self.values[count_data]:
                format_spec_d=f'>{len_col[count_len]}'
                string = string + f'{str(d):{format_spec_d}}' + " "
                count_len = count_len + 1
            count_len = 0
            count_data=count_data+1
            string = string + '\n'
        string = string[:-1]
        return string

    def __getitem__(self,col_list):
        newColumns=[]
        newDataSet=[]
        newData=[]
        newIndex=[]

        if isinstance(col_list,LabeledList):
            indexT = [i for i, x in enumerate(self.columns) if x in col_list]
            for it in indexT:
                newColumns.append(self.columns[it])
            for d in self.values:
                for it in indexT:
                    newData.append(d[it])
                newDataSet.append(newData)
                newData=[]
            newTable = Table(newDataSet, self.index, newColumns)
            return newTable

        elif isinstance(col_list, list):
            if isinstance(col_list[0], bool):
                indexT = [i for i, x in enumerate(col_list) if x is True]
                for it in indexT:
                    newIndex.append(self.index[it])
                    newDataSet.append(self.values[it])
                newTable = Table(newDataSet, newIndex, self.columns)
                return newTable
            else:
                indexT=[]
                for nc in col_list:
                    for i, x in enumerate(self.columns):
                        if x == nc:
                            indexT.append(i)
                for it in indexT:
                    newColumns.append(self.columns[it])
                for d in self.values:
                    for it in indexT:
                        newData.append(d[it])
                    newDataSet.append(newData)
                    newData=[]
                newTable = Table(newDataSet, self.index, newColumns)
                return newTable

        elif isinstance(col_list, int) or isinstance(col_list, float) or isinstance(col_list, str) or isinstance(col_list, bool):
            indexT = [i for i, x in enumerate(self.columns) if x in col_list]
            newData=[]
            newDataSet=[]
            newColumns
            if len(indexT) == 1:
                it=indexT[0]
                for d in self.values:
                    newData.append(d[it])
                return LabeledList(newData, self.index)
            else:
                for it in indexT:
                    newColumns.append(self.columns[it])
                for d in self.values:
                    for it in indexT:
                        newData.append(d[it])
                    newDataSet.append(newData)
                    newData=[]
                newTable = Table(newDataSet, self.index, newColumns)
                return newTable
        
    def head(self,n):
        newData=self.values[:n]
        newIndex=self.index[:n]
        return Table(newData, newIndex, self.columns)

    def tail(self,n):
        newData=self.values[-n:]
        newIndex=self.index[-n:]
        return Table(newData, newIndex, self.columns)

    def shape(self):
        x=len(self.values[0])
        y=len(self.values)
        xy_reversal = lambda x,y : (y,x)
        return xy_reversal(x,y)

def read_csv(fn):
    with open(fn,'r') as f:
        result = []
        for line in f:
            word = line.split(',')
            result.append(word)
    column = result[0]
    index = []
    data = []
    dataSet = []
    for r in result[1:]:
        for i in range(len(r)):
            r[i]=r[i].strip()
            if r[i].isdigit():
                r[i]=int(r[i])
                data.append(r[i])
            else:
                try:
                    float(r[i])
                    data.append(float(r[i]))
                except:
                    data.append(r[i])
        dataSet.append(data)
        data = []
    newTable = Table(dataSet, columns = column)
    return newTable
