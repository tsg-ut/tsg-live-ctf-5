#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#define LEN 8
#define FLAG "TSGLIVE{aU+0m4T10n_i2_d1FfIcu1t}"
unsigned long arr[LEN];
unsigned char cbuf[LEN*4+1];
int is_flag(){
  const unsigned long x[64]={
    22,
    56,
    53,
    59,
    21,
    55,
    7,
    12,
    37,
    3,
    46,
    14,
    35,
    17,
    30,
    2,
    60,
    20,
    58,
    49,
    32,
    40,
    13,
    4,
    34,
    54,
    5,
    48,
    51,
    44,
    47,
    9,
    11,
    19,
    18,
    38,
    41,
    24,
    33,
    61,
    36,
    52,
    8,
    50,
    26,
    10,
    25,
    16,
    23,
    42,
    29,
    28,
    62,
    0,
    31,
    1,
    45,
    39,
    63,
    27,
    57,
    43,
    15,
    6
  };
  const unsigned long mat[LEN][LEN]={{0, 12, 485, 101, 19, 32, 78, 150},
    {286, 49, 48, 85, 108, 59, 79, 244},
    {401, 62, 64, 31, 6, 6, 81, 12},
    {12, 597, 53, 28, 1, 9, 761, 31},
    {1, 155, 40, 59, 334, 261, 22, 23},
    {2, 13, 2, 13, 7, 105, 324, 72},
    {11, 4, 95, 6, 126, 76, 15, 5},
    {28, 13, 24, 30, 25, 99, 2, 118}};
  unsigned long ret[LEN]={
    739742811804,
    3314247231427,
    208803620379,
    356651854537,
    742309171906,
    2969711454506,
    108025436590,
    904845131517
  };
  for (size_t i = 0; i < LEN; i++) {
    unsigned long tmp=0;
    for (size_t j = 0; j < LEN; j++) {
      unsigned long tmp1=i*LEN+j;
      unsigned long tmp2=x[tmp1];
      size_t ii=tmp2/8,jj=tmp2%8;
      tmp+=arr[j]*mat[ii][jj];
    }
    if(tmp!=ret[i]){
      return 0;
    }
  }
  //if(0 == strcmp(cbuf,FLAG)){
  //  return 1;
  //}
  //return 0;
  return 1;
}
void win(){
  puts("you win!");
  return;
}
int main(){
  puts("hint:strlen(FLAG)==32,FLAG==\"TSGLIVE{...}\"");
  fgets(cbuf,LEN*4+1,stdin);
  if(cbuf[strlen(cbuf)-1]=='\n')cbuf[strlen(cbuf)-1]='\x00';
  for (int i = 0; i < LEN; i++) {
    arr[i]=*(int*)(cbuf+i*4);
  }
  if(is_flag()){
    win();
  }
  return 0;
}

