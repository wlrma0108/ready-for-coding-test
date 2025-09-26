#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int T; 


    if(!(cin >> T)) return 0;
    
    while (T--) {
        long long x1, y1, x2, y2;
        cin >> x1 >> y1 >> x2 >> y2;
        int n; cin >> n;
        int ans = 0;
        for (int i = 0; i < n; ++i) {
            long long cx, cy, r;
            cin >> cx >> cy >> r;
            long long dx1 = x1 - cx, dy1 = y1 - cy;
            long long dx2 = x2 - cx, dy2 = y2 - cy;
            long long d1 = dx1*dx1 + dy1*dy1;
            long long d2 = dx2*dx2 + dy2*dy2;
            long long rr = r*r;
            bool in1 = d1 < rr;
            bool in2 = d2 < rr;
            if (in1 ^ in2) ++ans;
        }
        cout << ans << "\n";
    }
    return 0;
}
