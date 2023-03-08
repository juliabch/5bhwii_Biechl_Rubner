public class BinarySearch {

    public static void binarySearch(char arr[], int first, int last, char val){

        if( first <= last ){
            //Ermittlung der Mitte des durchzusuchenden Arrays
            int mid = first + (last - first)/2;

            // (int) ... Typecast, funktioniert bei allem, das einen numerischen Wert dahinter hat

            // (int)arr[mid] holt sich den int-value (ascii) aus dem Array names arr[]
            // an der Position mid und überprüft ob der int kleiner ist als der Wert des gesuchten char
            if ( (int)arr[mid] < (int)val ){
                // der gesuchte Buchstabe ist größer,
                // daher wird first auf die aktuelle Mitte von arr[] gesetzt
                // +1 weil der searchval nicht gleich der Mitte ist
                first = mid + 1;
            }
            // else if für den Fall wenn, mid der gesuchte Buchstabe ist
            else if ( arr[mid] == val ){
                System.out.println("Element is found at index: " + mid);
            }
            // der gesuchte Buchstabe befindet sich in der ersten Hälfte des Arrays
            else{
                // wir setzten den letzten Index auf den Wert Mitte -1
                last = mid - 1;
            }
        }
        if ( first > last ){
            // Abbruchsbedingung, für den Abbruch der while()-Schleife
            System.out.println("Element is not found!");
        }
    }
    public static void main(String args[]){
        char arr[] = {'a','b','c','d','e','f','g','h','i'};
        char val = 'c';

        binarySearch(arr,0,arr.length-1,val);
    }

}






