import tensorflow as tf
hello=tf.constant('hello,tensorflow')
sess=tf.sess()
print(sess.run(hello))