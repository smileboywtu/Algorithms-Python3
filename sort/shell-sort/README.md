# Introduction
	
>shell sort is developed from the insert sort, but it can sort pairs of elements far apart from each other.

# Description
	
>### Example
> Array:  [1, 34, 23, 56, 87, 2, 67, 45, 5, 21]
>### Gaps
> you need gap to divide the source data into several groups.here i just pick some batter gaps for you.
>
> the array contains 10 elements. so we just use n/2 to get the proper gap
>
> [10/2, 5/2, 2/2]  => [5, 2, 1]
>### Details
>

>> ####pick gap 5
>>> the source data is divided into {1, 2}, {34, 67}, {23, 45}, {56, 5}, {87, 21}, here you need to just sort the serveral groups respectively.
>>>
>>> you will get the array:    [1, 34, 23, 5, 21, 2, 67, 45, 56, 87] after using gap 5 to sort.

>> ####pick gap 2
>>> the source data is divided into {1, 23, 21, 67, 56}, {34, 5, 2, 45, 87}, sort the 2 groups data respectively. 
>>>
>>> you will get the array:    [1, 2, 5, 21, 23, 34, 45, 56, 67, 87] after using gap 2 to sort.

>> ####pick gap 1
>>> because the gap is 1, you will get the only one group of data, the whole array.notice than every designed gap sequence must contains gap 1.
if you want to see more gaps, just read this [wikipedia](https://en.wikipedia.org/wiki/Shellsort).
>>>
>>> after sort you just get the right sort sequence: [1, 2, 5, 21, 23, 34, 45, 56, 67, 87].

>### Test

>>  we provide the C and Python code for this algorithm.let look at the c code here.
>>####Code C
        void shellsort(int v[], int n){
            int i, j;
            int gap;
            int temp;
            for(gap=n/2; gap>0; gap/=2){
                for(i=gap; i<n; i++){
                    temp = a[j];
                    for(j=i; (j-gap>=0)&&(v[j-gap]>temp); j-=gap){
                        v[j] = v[j-gap];
                    }
                    v[j] = temp;
                }
            }
        }
>>####Result
>>> Here I will print every gap result using this code
>>>
    printf("the current gap is %d\n", gap);
    for(i=0; i<n; i++){
        printf(" %d", v[i]);
    }
    putchar('\n');
>>>
>>> we will get:
>>>> the current gap is: 5
>>>>
>>>>  1 34 23 5 21 2 67 45 56 87
>>>>
>>>> the current gap is: 2
>>>>
>>>>  1 2 21 5 23 34 56 45 67 87
>>>>
>>>> the current gap is: 1
>>>>
>>>> 1 2 5 21 23 34 45 56 67 87



  
	
