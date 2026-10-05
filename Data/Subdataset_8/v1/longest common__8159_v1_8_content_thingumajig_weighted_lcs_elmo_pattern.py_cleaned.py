import tensorflow as tf
import tensorflow_hub as hub
import scipy.spatial.distance as distance
import logging
import sys
from patterns import Pattern, EmbeddingContext, SimpleWeight
class ElmoContext(EmbeddingContext):
    def __init__(self, spec='http:
        self.elmo = hub.Module(spec, trainable=False)
    def get_embedding_tensor(self, text):
        return self.__get_embedding_tensor([text])[0]
    def get_embedding_tensors(self, texts):
        return self.__get_embedding_tensor(texts)
    def get_compare_func(self):
        def cos_sim(x, y):
            return SimpleWeight(1 - distance.cosine(x, y))
        return cos_sim
    def __get_embedding_tensor(self, texts, type="elmo", signature="default"):
        embedding_tensor = self.elmo(texts, signature=signature, as_dict=True)[type]
        with tf.Session() as sess:
            sess.run(tf.global_variables_initializer())
            embedding = sess.run(embedding_tensor)
        return embedding
if __name__ == '__main__':
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.INFO)
    logger = logging.getLogger(__name__)
    logger.info(tf.__version__)
    ec = ElmoContext()
    ptext = 'ÐÑÐ°Ð²Ð¸ÑÐµÐ»ÑÑÑÐ²Ð¾ Ð ÐµÑÐ¿ÑÐ±Ð»Ð¸ÐºÐ¸ Ð¡ÑÐ´Ð°Ð½ Ð¸ ÐÑÐ°Ð²Ð¸ÑÐµÐ»ÑÑÑÐ²Ð¾ Ð ÐµÑÐ¿ÑÐ±Ð»Ð¸ÐºÐ¸ Ð®Ð¶Ð½ÑÐ¹ Ð¡ÑÐ´Ð°Ð½ Ð´Ð°Ð»ÐµÐµ Ð½Ð°Ð·ÑÐ²Ð°ÐµÐ¼ÑÐµ CÑÐ¾ÑÐ¾Ð½Ñ Ð¿ÑÐ¸Ð½Ð¸Ð¼Ð°ÑÑ Ð½Ð°ÑÑÐ¾ÑÑÐµÐµ Ð¡Ð¾Ð³Ð»Ð°ÑÐµÐ½Ð¸Ðµ'
    p = Pattern(ptext, 8, 11, embedding_context=ec)
    s = 'ÐÐ¾ÑÑÐ´Ð°ÑÑÑÐ²Ð° ÑÑÐ°ÑÑÐ½Ð¸ÐºÐ¸ Ð½Ð°ÑÑÐ¾ÑÑÐµÐ¹ ÐÐµÐºÐ»Ð°ÑÐ°ÑÐ¸Ð¸ Ð¸Ð¼ÐµÐ½ÑÐµÐ¼ÑÐµ Ð² Ð´Ð°Ð»ÑÐ½ÐµÐ¹ÑÐµÐ¼ CÑÐ¾ÑÐ¾Ð½Ñ Ð±ÑÐ´ÑÑ Ð¿ÑÐ¾Ð´Ð¾Ð»Ð¶Ð°ÑÑ ÑÐ°Ð·Ð²Ð¸Ð²Ð°ÑÑ Ð¸ ÑÐºÑÐµÐ¿Ð»ÑÑÑ ÑÐ¾ÑÑÑÐ´Ð½Ð¸ÑÐµÑÑÐ²Ð¾ ' \
        'Ð² Ð¾Ð±Ð»Ð°ÑÑÐ¸ ÑÐ°Ð·Ð²Ð¸ÑÐ¸Ñ Ð¶ÐµÐ»ÐµÐ·Ð½Ð¾Ð´Ð¾ÑÐ¾Ð¶Ð½Ð¾Ð³Ð¾ ÑÑÐ°Ð½ÑÐ¿Ð¾ÑÑÐ° Ð½Ð° ÐµÐ²ÑÐ¾Ð°Ð·Ð¸Ð°ÑÑÐºÐ¾Ð¼ Ð¿ÑÐ¾ÑÑÑÐ°Ð½ÑÑÐ²Ðµ Ð´Ð°Ð»ÐµÐµ Ð½Ð°Ð·ÑÐ²Ð°ÐµÐ¼ÑÐµ CÑÐ¾ÑÐ¾Ð½Ñ Ð¿ÑÐ¸Ð½Ð¸Ð¼Ð°ÑÑ Ð½Ð°ÑÑÐ¾ÑÑÐµÐµ Ð¡Ð¾Ð³Ð»Ð°ÑÐµÐ½Ð¸Ðµ'
    m = p.get_matcher_str(s)
    while True:
        w, span = m.find()
        if span is None:
            break
        print('span:{} w: {}'.format(span, w))
        print(p.get_string_from_span(span, s.split(), delimiter=' '))