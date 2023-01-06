'''
트리 (Tree)
Stack, Queue 가 선형적인 1차원적 자료구조 였다면 트리는 2차원의 자료 구조
정점 (node) 과 간선 (edge) 를 이용하여 데이터의 배치 형태를 추상화한 자료 구조

노드의 구분
1. root : 트리의 루트 노드
2. leaf : 트리의 제일 끝 노드
3. internal : root 와 leaf 사이에 있는 모든 노드
4. parent : edge 로 연결 된 노드들 간 root쪽에 가까운 노드
5. child : edge 로 연결 된 노드들 간 leaf쪽에 가까운 노드

노드의 관계
1. sibling : 같은 parent 를 가진 child nodes (형제 관계)
2. ancestor : 부모의 부모 (의 부모의...) 즉, 조상
3. descendant : 자식의 자식 (의 자식의...) 즉, 후손

노드의 수준 (level)
level0 의 root node 을 기준으로 하여 leaf 쪽으로 1단계씩 증가

트리의 높이 (height, depth) : max level + 1

서브 트리 (부분 트리)
트리 안에서 특정 노드 (root node 하위)를 중심으로 트리를 구성

노드의 차수 (Degree)
child(sub tree)의 수 (간선의 갯수)
leaf 로 향하는 간선은 하나 이상일 수 있지만 root 로 향하는 간선은 하나인 것이 트리의 구조가 가지는 성질
'''

'''
이진 트리 (Binary Tree)
모든 노드의 degree 가 2 이하인 트리

포화 이진 트리 (Full Binary Tree)
모든 레벨에서 노드들이 모두 채워져 있는 이진 트리
높이가 k 이고 노드의 개수가 2^k - 1

완전 이진 트리 (Complete Binary Tree)
높이 k인 완전 이진 트리
1. 레벨 k - 2 까지는 모든 노드가 2개의 자식을 가진 포화 이진 트리
2. 레벨 k - 1 에서는 왼쪽부터 노드가 순차적으로 채워져 있는 이진 트리
'''