# coding=utf-8

from flask_cors import CORS
from flask import Flask, jsonify, request

from entities.entity import Session, engine, Base

from entities.stock_entity import( 
    StockSchema, NewsSchema, aapl_table, amgn_table, axp_table, ba_table, cat_table,
    crm_table, csco_table, cvx_table, dis_table, dow_table, gs_table,
    hd_table, hon_table, ibm_table, intc_table, jnj_table, jpm_table,
    ko_table, mcd_table, mmm_table, mrk_table, msft_table, nke_table,
    pg_table, trv_table, unh_table, v_table, vz_table, wba_table, wmt_table,
    aapl_news_table, amgn_news_table, axp_news_table, ba_news_table, cat_news_table, crm_news_table,
    csco_news_table, cvx_news_table, dis_news_table, dow_news_table, gs_news_table, hd_news_table,
    hon_news_table, ibm_news_table, intc_news_table, jnj_news_table, jpm_news_table, ko_news_table,
    mcd_news_table, mmm_news_table, mrk_news_table, msft_news_table, nke_news_table, pg_news_table,
    trv_news_table, unh_news_table, v_news_table, vz_news_table, wba_news_table, wmt_news_table)

app = Flask(__name__)

#if __name__ == "__main__":
#    app.run(host='127.0.0.1', port=5000)

CORS(app)

# if needed, generate database schema
Base.metadata.create_all(engine)


@app.route('/aapl', endpoint='aapl')
@app.route('/amgn', endpoint='amgn')
@app.route('/axp', endpoint='axp')
@app.route('/ba', endpoint='ba')
@app.route('/cat', endpoint='cat')
@app.route('/crm', endpoint='crm')
@app.route('/csco', endpoint='csco')
@app.route('/cvx', endpoint='cvx')
@app.route('/dis', endpoint='dis')
@app.route('/dow', endpoint='dow')
@app.route('/gs', endpoint='gs')
@app.route('/hd', endpoint='hd')
@app.route('/hon', endpoint='hon')
@app.route('/ibm', endpoint='ibm')
@app.route('/intc', endpoint='intc')
@app.route('/jnj', endpoint='jnj')
@app.route('/jpm', endpoint='jpm')
@app.route('/ko', endpoint='ko')
@app.route('/mcd', endpoint='mcd')
@app.route('/mmm', endpoint='mmm')
@app.route('/mrk', endpoint='mrk')
@app.route('/msft', endpoint='msft')
@app.route('/nke', endpoint='nke')
@app.route('/pg', endpoint='pg')
@app.route('/trv', endpoint='trv')
@app.route('/unh', endpoint='unh')
@app.route('/v', endpoint='v')
@app.route('/vz', endpoint='vz')
@app.route('/wba', endpoint='wba')
@app.route('/wmt', endpoint='wmt')

@app.route('/aapl-news', endpoint='aapl-news')
@app.route('/amgn-news', endpoint='amgn-news')
@app.route('/axp-news', endpoint='axp-news')
@app.route('/ba-news', endpoint='ba-news')
@app.route('/cat-news', endpoint='cat-news')
@app.route('/crm-news', endpoint='crm-news')
@app.route('/csco-news', endpoint='csco-news')
@app.route('/cvx-news', endpoint='cvx-news')
@app.route('/dis-news', endpoint='dis-news')
@app.route('/dow-news', endpoint='dow-news')
@app.route('/gs-news', endpoint='gs-news')
@app.route('/hd-news', endpoint='hd-news')
@app.route('/hon-news', endpoint='hon-news')
@app.route('/ibm-news', endpoint='ibm-news')
@app.route('/intc-news', endpoint='intc-news')
@app.route('/jnj-news', endpoint='jnj-news')
@app.route('/jpm-news', endpoint='jpm-news')
@app.route('/ko-news', endpoint='ko-news')
@app.route('/mcd-news', endpoint='mcd-news')
@app.route('/mmm-news', endpoint='mmm-news')
@app.route('/mrk-news', endpoint='mrk-news')
@app.route('/msft-news', endpoint='msft-news')
@app.route('/nke-news', endpoint='nke-news')
@app.route('/pg-news', endpoint='pg-news')
@app.route('/trv-news', endpoint='trv-news')
@app.route('/unh-news', endpoint='unh-news')
@app.route('/v-news', endpoint='v-news')
@app.route('/vz-news', endpoint='vz-news')
@app.route('/wba-news', endpoint='wba-news')
@app.route('/wmt-news', endpoint='wmt-news')

def test():
    session = Session()

    if request.endpoint == 'aapl':
        stock_objects = session.query(aapl_table).all()
        # transforming into JSON-serializable objects
        schema = StockSchema(many=True)
    elif request.endpoint == 'amgn':
        stock_objects = session.query(amgn_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'axp':
        stock_objects = session.query(axp_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'ba':
        stock_objects = session.query(ba_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'cat':
        stock_objects = session.query(cat_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'crm':
        stock_objects = session.query(crm_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'csco':
        stock_objects = session.query(csco_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'cvx':
        stock_objects = session.query(cvx_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'dis':
        stock_objects = session.query(dis_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'dow':
        stock_objects = session.query(dow_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'gs':
        stock_objects = session.query(gs_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'hd':
        stock_objects = session.query(hd_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'hon':
        stock_objects = session.query(hon_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'ibm':
        stock_objects = session.query(ibm_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'intc':
        stock_objects = session.query(intc_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'jnj':
        stock_objects = session.query(jnj_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'jpm':
        stock_objects = session.query(jpm_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'ko':
        stock_objects = session.query(ko_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'mcd':
        stock_objects = session.query(mcd_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'mmm':
        stock_objects = session.query(mmm_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'mrk':
        stock_objects = session.query(mrk_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'msft':
        stock_objects = session.query(msft_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'nke':
        stock_objects = session.query(nke_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'pg':
        stock_objects = session.query(pg_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'trv':
        stock_objects = session.query(trv_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'unh':
        stock_objects = session.query(unh_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'v':
        stock_objects = session.query(v_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'vz':
        stock_objects = session.query(vz_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'wba':
        stock_objects = session.query(wba_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'wmt':
        stock_objects = session.query(wmt_table).all()
        schema = StockSchema(many=True)
    elif request.endpoint == 'aapl-news':
        stock_objects = session.query(aapl_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'amgn-news':
        stock_objects = session.query(amgn_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'axp-news':
        stock_objects = session.query(axp_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'ba-news':
        stock_objects = session.query(ba_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'cat-news':
        stock_objects = session.query(cat_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'crm-news':
        stock_objects = session.query(crm_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'csco-news':
        stock_objects = session.query(csco_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'cvx-news':
        stock_objects = session.query(cvx_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'dis-news':
        stock_objects = session.query(dis_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'dow-news':
        stock_objects = session.query(dow_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'gs-news':
        stock_objects = session.query(gs_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'hd-news':
        stock_objects = session.query(hd_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'hon-news':
        stock_objects = session.query(hon_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'ibm-news':
        stock_objects = session.query(ibm_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'intc-news':
        stock_objects = session.query(intc_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'jnj-news':
        stock_objects = session.query(jnj_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'jpm-news':
        stock_objects = session.query(jpm_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'ko-news':
        stock_objects = session.query(ko_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'mcd-news':
        stock_objects = session.query(mcd_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'mmm-news':
        stock_objects = session.query(mmm_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'mrk-news':
        stock_objects = session.query(mrk_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'msft-news':
        stock_objects = session.query(msft_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'nke-news':
        stock_objects = session.query(nke_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'pg-news':
        stock_objects = session.query(pg_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'trv-news':
        stock_objects = session.query(trv_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'unh-news':
        stock_objects = session.query(unh_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'v-news':
        stock_objects = session.query(v_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'vz-news':
        stock_objects = session.query(vz_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'wba-news':
        stock_objects = session.query(wba_news_table).all()
        schema = NewsSchema(many=True)
    elif request.endpoint == 'wmt-news':
        stock_objects = session.query(wmt_news_table).all()
        schema = NewsSchema(many=True)
    else: return "not valid"

    result = schema.dump(stock_objects)

    # serializing as JSON
    session.close()
    return jsonify(result)




'''@app.route('/exams', methods=['POST'])
def add_exam():
    # mount exam object
    posted_exam = ExamSchema(only=('date', 'price', 'change', 'changePercent'))\
        .load(request.get_json())

    exam = Exam(**posted_exam.data, created_by="HTTP post request")

    # persist exam
    session = Session()
    session.add(exam)
    session.commit()

    # return created exam
    new_exam = ExamSchema().dump(exam).data
    session.close()
    return jsonify(new_exam), 201'''
