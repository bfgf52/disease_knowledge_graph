# disease_knowledge_graph
�Լ�������һ���򵥵ļ���֪ʶͼ��  
## ʹ�õ�����
���ҽԺMMC�˹����ܸ�������֪ʶͼ�״����������ṩ�����ݼ���ʵ���ϵ�Լ�����������Ҫ�Լ���ȡ�����ʵ�����ϵ�����洢Ϊ����neo4j���õ���ʽ�����ݼ�  
## ʵ���ϵ�������  
1����鷽�� -> ������Test_Disease��  
2���ٴ����� -> ������Symptom_Disease��  
3����ҩ���� -> ������Treatment_Disease��  
4��ҩƷ���� -> ������Drug_Disease��  
5����λ -> ������Anatomy_Disease��  
6����ҩƵ�� -> ҩƷ���ƣ�Frequency_Drug��  
7������ʱ�� -> ҩƷ���ƣ�Duration_Drug��  
8����ҩ���� -> ҩƷ���ƣ�Amount_Drug��  
9����ҩ���� -> ҩƷ���ƣ�Method_Drug��  
10��������Ӧ -> ҩƷ���ƣ�SideEff-Drug��	  
## �������ݼ��ű�

process_data.py
## �������ݽű�
�������ݽű�.txt
## ����Ч��
![����Ч��](images/20190804165051.png)
## �Լ���дcypher��䲢���ؽ��չʾ
1��������Ҫ��Щҩ������
match (m:drug)-[r:drug_of]->(p:disease) where p.name = '1������' return m,p
![����Ч��](images/20190804164533.png)

