#include <bits/stdc++.h>

using namespace std;

class SegmentTree
{
private:
    int size;
    vector<int> segTree;

public:
    SegmentTree(int n) : size(n), segTree(2 * n, INT_MIN)
    {
    }
    void update(int pos, int val)
    {
        pos += size;
        segTree[pos] = val;
        while (pos > 0)
        {
            pos /= 2;
            segTree[pos] = max(segTree[2 * pos], segTree[2 * pos + 1]);
        }
    }

    int maxRange(int left, int right)
    {
        if (left > right)
            return INT_MIN;
        left += size;
        right += size;
        int res = INT_MIN;
        while (left <= right)
        {
            if (left % 2 == 1)
                res = max(res, segTree[left++]);
            if (right % 2 == 0)
                res = max(res, segTree[right--]);
            left /= 2;
            right /= 2;
        }
        return res;
    }
};