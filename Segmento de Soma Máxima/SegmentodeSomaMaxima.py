import math

def SegmentoSomaMaxima(A, low, mid, high):
    leftSum = -math.inf
    _sum = 0
    maxLeft = 0
    for i in range(mid, low, -1):
        _sum = _sum + A[i]
        if(_sum > leftSum):
            leftSum = _sum
            maxLeft = i

    rightSum = -math.inf
    _sum = 0
    maxRight = 0
    for i in range(mid + 1, high):
        _sum = _sum + A[i]
        if(_sum > rightSum):
            rightSum = _sum
            maxRight = i
    return maxLeft, maxRight, (leftSum + rightSum)

def Subarray(A, low, high):
    if high == low:
        return low, high, A[low]
    else:
        mid = int((low + high) / 2)

        leftLow, leftHigh, leftSum = Subarray(A, low, mid)
        rightLow, rightHigh, rightSum = Subarray(A, mid + 1, high)
        crossLow, crossHigh, crossSum = SegmentoSomaMaxima(A, low, mid, high)
        
        if((leftSum >= rightSum) and (leftSum >= crossSum)):
            return leftLow, leftHigh, leftSum
        elif((rightSum >= leftSum) and (rightSum >= crossSum)):
            return rightLow, rightHigh, rightSum
        else:
            return crossLow, crossHigh, crossSum
        
if __name__== "__main__":
    A = [-16, 20, -10, 12, 27, -6, -4, 8]
    print(Subarray(A, 0, len(A) - 1))