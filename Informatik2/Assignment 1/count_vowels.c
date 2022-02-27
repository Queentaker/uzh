void BSm(char A[1000]){
    int i,n;
    char BS[3000]={};
    char b='b';
    int h=0;
    n=strlen(A);
    for(i = 0; i <= n; i++){
        if(A[i] == 'a' || A[i] == 'e' || A[i] == 'i' || A[i] == 'o' || A[i] == 'u' ||
           A[i] == 'A' || A[i] == 'E' || A[i] == 'I'|| A[i] == 'O' || A[i] ==  'U') {
            BS[h]=A[i];
            BS[h+1]=b;
            BS[h+2]=A[i];
            h=h+3;
        }
        else{
            BS[h]=A[i];
            h+=1;
        }

        }
    int r=strlen(BS);
    int s=0;
    for (s;s<=r; s++){
        printf("%c",BS[s]);
    }


}
