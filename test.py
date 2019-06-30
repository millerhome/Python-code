
import tensorflow as tf
hello=tf.constant('hello,tensorflow 測試成功')
sess=tf.Session()
print(sess.run(hello))