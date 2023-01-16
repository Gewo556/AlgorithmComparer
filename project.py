def MergeSort(arr, iL, iR):
    if iL < iR:
        mid = (iL + iR)//2
        MergeSort(arr, iL, mid)
        MergeSort(arr, mid + 1, iR)
        Merge(arr, iL, mid, iR)
    return


def Merge(arr, iL, iM, iR):

    arr1 = arr[iL:iM+1].copy()
    arr2 = arr[iM+1:iR+1].copy()

    lenArr1 = len(arr1)
    lenArr2 = len(arr2)

    i = 0
    j = 0
    while 1>0:
        if i > lenArr1 - 1:
            for indexElement in range(j, lenArr2):
                arr[iL] = arr2[indexElement]
                iL += 1
            return

        if j > lenArr2 - 1:
            for indexElement in range(i, lenArr1):
                arr[iL] = arr1[indexElement]
                iL += 1
            return

        if arr1[i] <= arr2[j]:
            arr[iL] = arr1[i]
            i += 1
            iL += 1
        else:
            arr[iL] = arr2[j]
            j += 1
            iL += 1