
    feat_extractor = ResNet50(weights='imagenet', include_top=False, input_shape=(224, 224, 3), pooling='avg')