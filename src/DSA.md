# 二叉树

## 二叉树结构

```cpp
struct TreeNode
{
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode() : val(0), left(nullptr), right(nullptr) {}
    TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
    TreeNode(int x, TreeNode* left, TreeNode* right) : val(x), left(left), right(right) {}
};
```


## N叉树结构

```cpp
class Node
{
public:
    int val;
    vector<Node*> children;

    Node() {}

    Node(int _val)
    {
        val = _val;
    }

    Node(int _val, vector<Node*> _children)
    {
        val = _val;
        children = _children;
    }
};
```


## 翻转

```cpp
void Reverse(vector<int>& result)
{
    for (int i = 0, j = result.size() - 1; i < j; ++i, --j)
    {
        int temp = result[i];
        result[i] = result[j];
        result[j] = temp;
    }
}
```


## 二叉树遍历

### 递归

#### 前序遍历

```c++
void traversal(TreeNode* root, vector<int>& result)
{
    if (root == nullptr) return;
    result.push_back(root->val);
    traversal(root->left, result);
    traversal(root->right, result);
}
vector<int> preorderTraversal(TreeNode *root)
{
    vector<int> result;
    traversal(root, result);
    return result;
}
```

#### 后序遍历

```c++
void traversal(TreeNode* root, vector<int>& result)
{
    if (root == nullptr) return;
    traversal(root->left, result);
    traversal(root->right, result);
    result.push_back(root->val);
}
vector<int> postorderTraversal(TreeNode* root)
{
    vector<int> result;
    traversal(root, result);
    return result;
}
```

#### 中序遍历

```c++
void traversal(TreeNode* root, vector<int>& result)
{
    if (root == nullptr) return;
    traversal(root->left, result);
    result.push_back(root->val);
    traversal(root->right, result);
}
vector<int> inorderTraversal(TreeNode* root)
{
    vector<int> result;
    traversal(root, result);
    return result;
}
```


### 迭代

#### 前序遍历

##### （方法一）

```c++
vector<int> preorderTraversal(TreeNode* root) 
{
    vector<int> result;
    if(root==nullptr) return result;
    stack<TreeNode*> st_TreeNode;
    st_TreeNode.push(root);
    while(!st_TreeNode.empty())
    {
        TreeNode* node=st_TreeNode.top();
        st_TreeNode.pop();
        result.push_back(node->val);
        if(node->right!=nullptr) st_TreeNode.push(node->right);
        if(node->left!=nullptr) st_TreeNode.push(node->left);   
    }
    return result;
}
```

##### （方法二）

```c++
vector<int> preorderTraversal(TreeNode* root)
{
    vector<int> result;
    if (root == nullptr)
        return result;
    stack<TreeNode*> st_TreeNode;
    TreeNode* node = root;
    while (node != nullptr || !st_TreeNode.empty())
    {
        while (node != nullptr)
        {
            st_TreeNode.push(node);
            result.push_back(node->val);
            node = node->left;
        }
        if (!st_TreeNode.empty())
        {
            node = st_TreeNode.top();
            st_TreeNode.pop();
            node = node->right;
        }
    }
    return result;
}
```


#### 后序遍历

##### （方法一）

```c++
vector<int> postorderTraversal(TreeNode* root)
{
    vector<int> result;
    if (root == nullptr)
        return result;
    stack<TreeNode*> st_TreeNode;
    st_TreeNode.push(root);
    while (!st_TreeNode.empty())
    {
        TreeNode* node = st_TreeNode.top();
        st_TreeNode.pop();
        result.push_back(node->val);
        if (node->left != nullptr)
            st_TreeNode.push(node->left);
        if (node->right != nullptr)
            st_TreeNode.push(node->right);
    }
    Reverse(result);
    return result;
}
```

##### （方法二）

```c++
vector<int> postorderTraversal(TreeNode* root)
{
    vector<int> result;
    if (root == nullptr)
        return result;
    stack<TreeNode*> st_TreeNode;
    TreeNode* node = root;
    while (node != nullptr || !st_TreeNode.empty())
    {
        while (node != nullptr)
        {
            st_TreeNode.push(node);
            result.push_back(node->val);
            node = node->right;
        }
        if (!st_TreeNode.empty())
        {
            node = st_TreeNode.top();
            st_TreeNode.pop();
            node = node->left;
        }
    }
    Reverse(result);
    return result;
}
```


#### 中序遍历（只有方法二）

```c++
vector<int> inorderTraversal(TreeNode* root)
{
    vector<int> result;
    if (root == nullptr)
        return result;
    stack<TreeNode*> st_TreeNode;
    TreeNode* node = root;
    while (node != nullptr || !st_TreeNode.empty())
    {
        while (node != nullptr)
        {
            st_TreeNode.push(node);
            node = node->left;
        }
        if (!st_TreeNode.empty())
        {
            node = st_TreeNode.top();
            st_TreeNode.pop();
            result.push_back(node->val);
            node = node->right;
        }
    }
    return result;
}
```

#### 层序遍历（BFS）

```c++
vector<vector<int>> levelOrder(TreeNode* root)
{
    vector<vector<int>> result;
    if (root == nullptr)
        return result;
    queue<TreeNode*> que_TreeNode;
    que_TreeNode.push(root);
    while (!que_TreeNode.empty())
    {
        int size = que_TreeNode.size();
        vector<int> temp;
        for (int i = 0; i != size; ++i)
        {
            TreeNode* node = que_TreeNode.front();
            que_TreeNode.pop();
            temp.push_back(node->val);
            if (node->left != nullptr)
                que_TreeNode.push(node->left);
            if (node->right != nullptr)
                que_TreeNode.push(node->right);
        }
        result.push_back(temp);
    }
    return result;
}
```
# 排序
## 交换swap

```cpp
void swap(int& a, int& b)
{
	int temp = a;
	a = b;
	b = temp;
}

void swap(int& a, int& b)
{
	a = a ^ b;
	b = a ^ b;
	a = a ^ b;
}
```


## 冒泡排序 O(n^2)

### 一

isSort：是否已经有序的标志

```cpp
void Bubble_Sort(vector<int>& nums)
{
	for (int end = nums.size() - 1; end > 0; end--)
	{
		bool isSort = true;
		for (int i = 0; i < end; i++)
		{
			if (nums[i] > nums[i + 1])
			{
				swap(nums[i], nums[i + 1]);
				isSort = false;
			}
		}
		if (isSort) break;
	}
}
```

### 二

border：记录上一次最后交换的位置，下一轮交换只需要进行到这个位置即可

```cpp
void Bubble_Sort(vector<int>& nums)
{
	for (int end = nums.size() - 1; end > 0; end--)
	{
		int border = 0;
		for (int i = 0; i < end; i++)
		{
			if (nums[i] > nums[i + 1])
			{
				swap(nums[i], nums[i + 1]);
				border = i + 1;
			}
		}
		end = border;
	}
}
```

### 三

鸡尾酒排序：定向冒泡排序，同时的冒泡两边

```cpp
void Bubble_Sort(vector<int>& nums)
{
	int left = 0, right = nums.size() - 1;
	while (left < right)
	{
		for (int i = left; i < right; i++)
		{
			if (nums[i] > nums[i + 1])
			{
				swap(nums[i], nums[i + 1]);
			}
		}
		right--;

		for (int i = right; i > left; i--)
		{
			if (nums[i] < nums[i - 1])
			{
				swap(nums[i - 1], nums[i]);
			}
		}
		left++;
	}
}
```


## 选择排序 O(n^2)

每次从待排序列中选出一个最小值，然后放在序列的起始位置，直到全部待排数据排完即可。

```cpp
void Select_Sort(vector<int>& nums)
{
	for (int i = 0; i < nums.size(); i++)
	{
		int start = i, min = i;
		while (start < nums.size())
		{
			if (nums[start] < nums[min]) min = start;
			start++;
		}
		if (min != i) swap(nums[i], nums[min]);
	}
}
```


## 插入排序 O(n^2)

在待排序的元素中，假设前n-1个元素已有序，现将第n个元素插入到前面已经排好的序列中，使得前n个元素有序。按照此法对所有元素进行插入，直到整个序列有序。

```cpp
void Insert_Sort(vector<int>& nums)
{
	for (int i = 1; i < nums.size(); i++)
	{
		int insert_value = nums[i];
		int insert_pos = i;
		while (insert_pos > 0 && nums[insert_pos - 1] > insert_value)
		{
			nums[insert_pos] = nums[insert_pos - 1];
			insert_pos--;
		}
		nums[insert_pos] = insert_value;
	}
}
```


## 归并排序 O(nlogn)

将已有序的子序合并，从而得到完全有序的序列，即先使每个子序有序，再使子序列段间有序。

```cpp
void merge(vector<int>& nums, int left, int mid, int right) // 左闭右闭
{
	vector<int> left_nums;
	vector<int> right_nums;

	for (int i = left; i <= right; i++)
	{
		if (i <= mid) left_nums.push_back(nums[i]);
		else right_nums.push_back(nums[i]);
	}

	int i = 0, j = 0, k = left;
	while (i < left_nums.size() && j < right_nums.size())
	{
		if (left_nums[i] < right_nums[j])
		{
			nums[k] = left_nums[i];
			k++;
			i++;
		}
		else
		{
			nums[k] = right_nums[j];
			k++;
			j++;
		}
	}
	while (i < left_nums.size())
	{
		nums[k] = left_nums[i];
		k++;
		i++;
	}
	while (j < right_nums.size())
	{
		nums[k] = right_nums[j];
		k++;
		j++;
	}
}

void Merge_Sort(vector<int>& nums, int left, int right) // 左闭右闭
{
	if (left == right) return;
	else
	{
		int mid = left + (right - left) / 2;
		Merge_Sort(nums, left, mid);
		Merge_Sort(nums, mid + 1, right);
		merge(nums, left, mid, right);
	}
}
```


## 堆排序 O(nlogn)

```cpp
void heapify(vector<int>& nums, int nums_size, int root)
{
	if (root >= nums_size) return;
	int left_child = root * 2 + 1;
	int right_child = root * 2 + 2;
	int max = root;
	if (left_child < nums_size && nums[left_child] > nums[max])
	{
		max = left_child;
	}
	if (right_child < nums_size && nums[right_child] > nums[max])
	{
		max = right_child;
	}
	if (max != root)
	{
		swap(nums[root], nums[max]);
		heapify(nums, nums_size, max);
	}
}

void Heap_Sort(vector<int>& nums)
{
	// build heap
	int last_node = nums.size() - 1;
	int parent = (last_node - 1) / 2;
	for (int i = parent; i >= 0; i--)
	{
		heapify(nums, nums.size(), i);
	}

	// sort
	for (int i = nums.size() - 1; i >= 0; i--)
	{
		swap(nums[i], nums[0]);
		heapify(nums, i, 0);
	}
}
```


## 希尔排序

先选定一个小于nums.size()的整数gap作为第一增量，然后将所有距离为gap的元素分在同一组，并对每一组的元素进行直接插入排序。然后再取一个比第一增量小的整数作为第二增量，重复上述操作…

当增量的大小减到1时，就相当于整个序列被分到一组，进行一次直接插入排序，排序完成。

```cpp
void Shell_Sort(vector<int>& nums)
{
	// 初始增量gap=len/2，每一趟之后除以二
	for (int gap = nums.size() / 2; gap > 0; gap /= 2)
	{
		//插入排序
		for (int i = gap; i < nums.size(); i++)
		{
			int insert_value = nums[i];
			int insert_pos = i;
			while (insert_pos >= gap && nums[insert_pos - gap] > insert_value)
			{
				nums[insert_pos] = nums[insert_pos - gap];
				insert_pos -= gap;
			}
			nums[insert_pos] = insert_value;
		}
	}
}
```


## 快速排序 O(nlogn)

任取待排序元素序列中的某元素作为基准值，按照该基准值将待排序列分为两子序列，左子序列中所有元素均小于基准值，右子序列中所有元素均大于基准值，然后左右序列重复该过程，直到所有元素都排列在相应位置上为止。

```cpp
int partition(vector<int>& nums, int left, int right) // 左闭右闭
{
	int pivot = nums[right];
	int i = left;
	for (int j = left; j < right; j++)
	{
		if (nums[j] <= pivot)
		{
			swap(nums[i], nums[j]);
			i++;
		}
	}
	swap(nums[i], nums[right]);
	return i;
}

void Quick_Sort(vector<int>& nums, int left, int right) // 左闭右闭
{
	if (left < right)
	{
		int mid = partition(nums, left, right);
		Quick_Sort(nums, left, mid - 1);
		Quick_Sort(nums, mid + 1, right);
	}
}
```

### 二路快排

```cpp
void quicksort(vector<int>& nums, int left, int right) {
	if(left >= right) return;
	int pivot = nums[left];
	int i = left, j = right;
	while(i < j) {
		while(i < j && nums[j] > pivot) --j;
		while(i < j && nums[i] <= pivot) ++i;
		if(i < j) swap(nums[i], nums[j]);
	}
	swap(nums[left], nums[i]);
	quicksort(nums, left, i - 1);
    quicksort(nums, i + 1, right);
}
```

快速排序尽量使得分开的左右两区间大小一致，否则会退化为 `n^2` 的复杂度

- 当数据已基本有序时，pivot默认选最左边或最右边时，相当于每次只排序一个元素，退化为选择排序，应随机选择一个元素作为 pivot。

```cpp
void quicksort(vector<int>& nums, int left, int right) {
	if(left >= right) return;
	srand(time(nullptr));
	int random = rand() % (right - left + 1) + left;
	swap(nums[left], nums[random]);
	int pivot = nums[left];
	int i = left, j = right;
	while(i < j) {
		while(i < j && nums[j] > pivot) --j;
		while(i < j && nums[i] <= pivot) ++i;
		if(i < j) swap(nums[i], nums[j]);
	}
	swap(nums[left], nums[i]);
	quicksort(nums, left, i - 1);
    quicksort(nums, i + 1, right);
}
```

### 三路快排

- 当数据包含大量的重复元素，不论 pivot 如何选择，都会导致左右区间的大小严重失衡，应选择三路排序：分成三个区间，左（小于pivot） ，中（等于pivot），右（ 大于pivot），这样左右区间的大小不会相差太大。


```cpp
void quicksort(vector<int>& nums, int left, int right) {
	if(left >= right) return;
	srand(time(nullptr));
	int random = rand() % (right - left + 1) + left;
	swap(nums[left], nums[random]);
	int pivot = nums[left];
	int i = left + 1, j = right; // 中区间 [i, j]
	for(int k = left + 1; k <= j;) {
		if(nums[k] < pivot) {
			swap(nums[k], nums[i]);
			++i;
			++k;
		} else if(nums[k] == pivot) {
			++k;
		} else {
			swap(nums[k], nums[j]);
			--j;
		}
	}
	swap(nums[left], nums[i - 1]);
	quicksort(nums, left, i - 2);
    quicksort(nums, j + 1, right);
}
```