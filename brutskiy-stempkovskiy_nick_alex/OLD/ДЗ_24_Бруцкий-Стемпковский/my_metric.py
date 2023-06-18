"""
Подсчёт метрики IOU на масках изображения
"""
import tensorflow as tf


def iou(y_true, y_pred):
    """
    Функция для подсчёта метрики IOU на масках изображения
    """
    y_true_f = tf.keras.backend.flatten(y_true)
    y_pred_f = tf.keras.backend.flatten(y_pred)
    intersection = tf.keras.backend.sum(y_true_f * y_pred_f)
    return (2. * intersection + 1.0) / (tf.keras.backend.sum(y_true_f) \
                                         + tf.keras.backend.sum(y_pred_f) + 1.0)
