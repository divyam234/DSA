# Rotten Oranges

## Intuition

![Solution](https://assets.leetcode.com/uploads/2019/02/16/oranges.png)


[Practice Link](https://leetcode.com/problems/rotting-oranges)

**Code:** 

```java
 class Solution {
   
        public boolean isValid(int x,int y,int r,int c){
            return (0 <=x && x< r) && (0 <=y && y< c) ;
        }
        public int orangesRotting(int[][] grid) {

            int r= grid.length, c=grid[0].length;

            int[] X= {1,-1,0,0};

            int[] Y={0,0,-1,1};

            int ans=0,fresh=0;
            
            Queue<int[]> q = new LinkedList<>();

            for(int i=0;i<r;i++){
                for(int j=0;j<c;j++){
                    if (grid[i][j]==2) q.add(new int[]{i,j,0});

                    if (grid[i][j]==1) fresh+=1;
                }
            }

            while (!q.isEmpty()){
                
                int[] e= q.poll();
                
                int dis=e[2],x=e[0],y=e[1];
                
                ans=Math.max(dis,ans);

                for (int k=0;k<4;k++){
                    if ( isValid(x+X[k],y+Y[k],r,c) && grid[x+X[k]][y+Y[k]]==1){
                        
                        grid[x+X[k]][y+Y[k]]=2;
                        q.add(new int []{x+X[k],y+Y[k],dis+1});
                        fresh-=1;
                    }

                }
            }
            return fresh>0 ? -1: ans;
        }
    }

```