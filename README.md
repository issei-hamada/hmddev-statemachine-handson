# hmddev-statemachine-handson

## 概要

AWS Step Functions の使い方を学ぶ為の、簡単なテンプレートです。

## 動作環境

- Python 3.11
- AWS CLI v2
- AWS SAM

## 前提条件

- Python 3.11 がインストール済みである事
- AWS CLI がインストール済みである事
- AWS の credentials がセットしてある事
- AWS SAM がインストール済みである事

## デプロイ

template.yaml の存在するディレクトリで以下コマンドを実行

> sam deploy --guided --profile xxxxxx

## ハンズオン

1. AWS Step Functions の input の扱いを見る
2. input の値に応じて処理を分岐する
3. Step Functions から AWS API を実行する
4. Lambda なしで同じ処理を行う

### AWS Step Functions の input の扱いを見る

目的: input の扱われ方を学んで、基本的なフローの作り方を理解する

1. AWS Step Functions のコンソールへ遷移
2. 当該 State Machine を選択
3. 「実行を開始」を押下し、 event.json の中身をコピー&ペースト
4. 実行ログから以下を確認する
   - input がどのようにタスクへ引き渡されているか
   - input がどのように Lambda 内の event に引き渡されるか
   - Lambda からの Output はどのように扱われるか

### input の値に応じて処理を分岐する

目的: input の値から任意のタスクを実行する方法を学んで、ワークフロー内での実行制御の方法を理解する

1. AWS Step Functions のコンソールへ遷移
2. 当該 State Machine を選択
3. 「編集」を押下
4. ワークフロービルダーにて「フロー」 > 「Choice」を選択し、「Function」の前にドロップ
   - Rule#1 と Default に分かれる
5. 「フロー」 > 「Pass」を選択し、「Rule#1」の直下(ここに状態をドロップと書いてあるところ)にドロップ
6. 「Choice」を選択し、「Rule#1」を編集
7. 「Add conditions」でルールを作成する
   - Variable: "$.detail.findings[0].Severity.Normalized"
   - Operator: is grater than or equal to
   - Value: Number constant
   - 70
   - 条件を保存する
   - 「Then next state is」にて「Function」を選択
8. 「Default」ルールを編集し、Default State を 「Pass」に変更
9. 「実行を開始」を押下し、 event.json の中身をコピー&ペースト
10. 実行ログから以下を確認する
    - Choice が想定の挙動をしているか
    - event の中身を修正した場合、想定通り処理が変わるか

### Step Functions から AWS API を実行する

目的: AWS Step Functions 内で直接 AWS API を実行する方法を学ぶ

1. AWS Step Functions のコンソールへ遷移
2. 当該 State Machine を選択
3. 「実行を開始」を押下し、 event.json の中身をコピー&ペースト
4. 実行ログから以下を確認する
   - どうやって AWS API の求めているペイロードを指定しているか
   - SNS の件名・本文を変えるにはどうするか

### Lambda なしで同じ処理を行う

1. 以下をクローン
   > git clone https://github.com/issei-hamada/security-hub-aggregator.git
2. AWS SAM でデプロイ
3. AWS Step Functions のコンソールへ遷移
4. 当該 State Machine を選択
5. 「実行を開始」を押下し、 event.json の中身をコピー&ペースト
6. 実行ログから以下を確認する
   - どうやって処理を分岐しているか
   - どうやって json を整形しているか
