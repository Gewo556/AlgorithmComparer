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


def Menu():
    option1 = input('Jeśli chcesz wczytać dane z klawiatury wciśnij "1" i zatwierdź, \na jeśli chcesz wpisać dane z pliku wciśnij "2" i zatwierdź!\n')

    while option1 != "1" and option1 != "2":
        print("Błąd liczby. Podaj jeszcze raz!\n")
        option1 = input('Jeśli chcesz wczytać dane z klawiatury wciśnij "1" i zatwierdź, \na jeśli chcesz wpisać dane z pliku wciśnij "2" i zatwierdź!\n')
    
    date = []

    while True:
        date = []
        try:
            if option1 == "1":      #Klawiatura
                print("Ile danych chcesz wprowadzić?")
                dateCount = input()
                print("Wprowadź " + str(int(dateCount)) +" wartości. Każdą potwierdź enterem:")
                for i in range (0, int(dateCount)):
                    date.append(int(input()))
                break
            elif option1 == "2":    #Plik
                print("Podaj nazwę pliku(plik musi znajdować się w folderze): ")
                path = str(input())
                
                file = open(path)
                content = file.read()
                file.close()
                dateContent = content.split()
                
                for elements in dateContent:
                    date.append(int(elements))
                break
        except:
            print("Błąd, spróbuj jeszcze raz\n")

    dateMS = date.copy()
    dateQSR = date.copy()
    dateQSM = date.copy()

    print("Merge Sort:")
    #def Merge Sort
    #def Licznik czasu
    print("QuickSort z losowym wyborem elementu dzielącego\n")
    #def QuickSort z losowym wyborem elementu dzielącego
    #def Licznik czasu
    print("QuickSort z wyborem mediany jako elementu dzielącego\n")
    #def QuickSort z wyborem mediany jako elementu dzielącego
    #def Licznik czasu

    return