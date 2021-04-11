Emotional Chat Machine Pro

## Environment

- win10
- python 3.5
- tensorflow 0.12 / tensorflow-gpu 0.12
- cudn8.0
- cudnn5.1

硬件配置Intel Core i5-7500 / Nvidia Geforce GTX 1050 Ti

（注意pip的版本会影响可以安装的tensorflow版本）

（如果使用cpu训练，选取tensorflow，如果使用gpu训练，请使用tensorflow-gpu）

## Problem Record

- [x] 1.文件缺失

- train_data/multi_embedding.mat
- train_data/senti_embeddng

解决方案：直接注释掉就行了，这两个只是用来提升性能的，pre_train



- [x] 2.tf.one_hot()函数实现有bug
- 解决方案：在使用这个函数时，需要切换到CPU运行



- [x] 3.reponse全部为空
- train过程中，读写文件模式没有全部使用utf-8



- [x] 4.训练结果response的语义连贯性很差

解决方案：将post/response的大小从10000升级到20000。将训练的总条数从1million=>2million



- [x] 5.系统报错「cell must be an instance of RNNCell」

解决方案：因为在框架中重构了RNNCell，所以直接把原本的RNNCell校验的那6行逻辑删除掉就行了。