/*
// Problem: $(PROBLEM)
// Contest: $(CONTEST)
// Judge: $(JUDGE)
// URL: $(URL)
// Memory Limit: $(MEMLIM)
// Time Limit: $(TIMELIM)
// Start: $(DATE)
*/

#include <bits/stdc++.h>
using namespace std;
#define int long long
#define fast                        \
  ios_base::sync_with_stdio(false); \
  cin.tie(0);                       \
  cout << setprecision(12) << fixed;
#define rep(i, begin, end)                            \
  for (__typeof(end) i = (begin) - ((begin) > (end)); \
       i != (end) - ((begin) > (end)); i += 1 - 2 * ((begin) > (end)))
// __builtin_ffs(x) it return least significant digit index

#define f(i, a, b) for (int i = a; i < b; i++)
const int N = 1e5 + 1;
const int mod = 1e9 + 7;
const int inf = 2e18;

template <typename t1, typename t2>
istream &operator>>(istream &istream, pair<t1, t2> &p) {
  return (istream >> p.first >> p.second);
}

template <typename t>
istream &operator>>(istream &istream, vector<t> &v) {
  for (auto &it : v) {
    cin >> it;
  }
  return istream;
}

template <typename t1, typename t2>
ostream &operator<<(ostream &ostream, const pair<t1, t2> &p) {
  return (ostream << p.first << " " << p.second);
}

template <typename t>
ostream &operator<<(ostream &ostream, const vector<t> &c) {
  for (auto &it : c) cout << it << " ";
  return ostream;
}

int lcm(int a, int b) { return a * b / __gcd(a, b); }

void helper() {
  
}

int32_t main() {
  fast int t = 1;
  // cin>>t;
  while (t--) {
    helper();
  }
}
