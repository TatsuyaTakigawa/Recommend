from recommend_model import *

# トレーニング用のCSVを読み込む
df_user = pd.read_csv("data.csv")

dataset = tf.data.Dataset.from_tensor_slices({
    "user_id": df_user["USER_ID"].astype(str).tolist(),
    "item_id": df_user["ITEM_ID"].astype(str).tolist()
})

train_data = dataset.shuffle(10000).batch(128).cache()

# モデルのインスタンス化
model = RecommenderModel()
model.compile(optimizer=tf.keras.optimizers.Adagrad(0.5))

# 学習
model.fit(train_data, epochs=5,verbose=1)

# モデルの保存
model.save_weights('weights', save_format='tf')
