#include <stdio.h>
int main()
{
    int arr[8][8];
    int i = 0, j = 0, m, a, c, x, y;
    printf("Enter array\n");
    for (i = 0; i < 8; i++)
        for (j = 0; j < 8; j++)
            scanf("%d", &arr[i][j]);
    for (i = 0; i < 4; i++)
    {
        for (j = 0; j < 4; j++)
        {
            m = arr[i * 2][j * 2];
            x = i * 2;
            y = j * 2;
            a = i * 2;
            c = j * 2;
            if (arr[a][c + 1] < m)
            {
                m = arr[a + 1][c];
                x = a;
                y = c + 1;
            }
            if (arr[a + 1][c] < m)
            {
                m = arr[a + 1][c];
                x = a + 1;
                y = c;
            }
            if (arr[a + 1][c + 1] < m)
            {
                m = arr[a + 1][c + 1];
                x = a + 1;
                y = c + 1;
            }
            printf("(%d %d)\t", x, y);
        }
        printf("\n");
    }
}
