#include <bits/stdc++.h>

using namespace std;

#define ll long long int
#define rep(i, a, b) for(int i = a; i < b; i++)
#define rep0(i, a) for(int i = 0; i < a; i++)
#define rrep(i, b, a) for(int i = b; i > a; i--)
#define rrep0(i, a) for(int i = a; i >= 0; i--)

const int MxN = 101;
int n;
int a[MxN];

void solve();
int rev(int , int);

int main()
{
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    solve();

    return 0;
}

void solve() {
	int T;
	cin >> T;
	rep0(t, T) {
		cin >> n;
		rep0(i, n) {
			cin >> a[i];
		}

		int j, count = 0;
		rep0(i, n - 1) {
			j = i;
			rep(k, i, n) {
				if (a[k] < a[j]) {
					j = k;
					// cout << ".";
				}
			}
			// cout << endl << i << "--" << j << endl;
			count += rev(i, j);
			rep0(x, n) {
				// cout << a[x] << " ";
			}
		}

		cout << "Case #" << (t + 1) << ": " << count << endl;
		rep0(x, n) {
			// cout << a[x] << " ";
		}
	}
}

int rev(int i, int j) {
	int c = j - i + 1;
	// cout << "c = " << c << endl;
	int l = (j - i) % 2 == 0 ? ((j - i) / 2) : ((j - i) / 2) + 1;
	// cout << "l = " << l << endl;
	rep0(k, l) {
		// cout << "k = " << k << endl;
		int temp = a[i + k];
		a[i + k] = a[j - k];
		a[j - k] = temp;
		// c++;
	}
	return c;
}