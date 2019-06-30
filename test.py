
import tensorflow as tf
hello=tf.constant('hello,tensorflow success')
sess=tf.Session()
print(sess.run(hello))
