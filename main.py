from pathlib import Path
import numpy as np
from PIL import Image
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


def load_dataset(root: str, max_per_class: int = 20):
    X, y = [], []
    classes = []
    class_dirs = [p for p in Path(root).rglob('*') if p.is_dir()]
    for dir_path in sorted(class_dirs):
        images = list(dir_path.glob('*.png')) + list(dir_path.glob('*.jpg'))
        if not images:
            continue
        label = dir_path.name
        if label not in classes:
            classes.append(label)
        for img_path in images[:max_per_class]:
            try:
                img = Image.open(img_path).convert('RGB').resize((32, 32))
            except Exception:
                continue
            X.append(np.asarray(img).flatten())
            y.append(classes.index(label))
    return np.array(X), np.array(y), classes


def main():
    X, y, classes = load_dataset('dataset')
    print(f"Loaded {len(X)} images across {len(classes)} classes.")
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LogisticRegression(max_iter=1000)
    model.fit(X_train, y_train)
    preds = model.predict(X_test)
    acc = accuracy_score(y_test, preds)
    print(f"Test accuracy: {acc:.2f}")


if __name__ == '__main__':
    main()
