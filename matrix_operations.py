import numpy as np
import psutil
import time
import random
from memory_profiler import memory_usage

class COOMatrix:
    def __init__(self,rows,cols):
        self.rows=rows
        self.cols=cols
        self.rowIndices=[]
        self.colIndices=[]
        self.values=[]
    def addValue(self,row,col,value):
        if value != 0:
            self.rowIndices.append(row)
            self.colIndices.append(col)
            self.values.append(value)
    def multiply(self,B):
        if self.cols==B.rows:
            result=COOMatrix(self.rows,B.cols)
            tempResult=np.zeros((self.rows,B.cols),dtype = int)
            for i in range(0,len(self.values),1):
                rowA=self.rowIndices[i]
                colA=self.colIndices[i]
                valA=self.values[i]
                for j in range(0,len(B.values),1):
                    if B.rowIndices[j]==colA:
                        colB=B.colIndices[j]
                        valB=B.values[j]
                        tempResult[rowA,colB]+= valA*valB
            for i in range(0,self.rows,1):
                for j in range(0,B.cols,1):
                    if tempResult[i,j]!=0:
                        result.addValue(i,j,tempResult[i,j])
            return result


def convertToCOO(matrix, N):
    cooMatrix = COOMatrix(N, N)
    density = 0.1

    for i in range(N):
        for j in range(N):
            if random.random() < density:
                value = matrix[i, j]
                if value != 0:
                    cooMatrix.addValue(i, j, value)
    return cooMatrix

def matrix_multiply(A,B):
    resultMatrix=A.multiply(B)
    return resultMatrix

def track_memory(func, *args):
    mem_usage = memory_usage((func, args))
    print(f"Memory usage: {max(mem_usage)} MB")
    return mem_usage

def track_cpu(func, *args):
    cpu_percent_before = psutil.cpu_percent(interval=1)
    start_time = time.time()

    func(*args)

    end_time = time.time()
    cpu_percent_after = psutil.cpu_percent(interval=1)

    print(f"Initial CPU usage: {cpu_percent_before}%")
    print(f"Final CPU usage: {cpu_percent_after}%")
    print(f"Execution time: {end_time - start_time} seconds")
