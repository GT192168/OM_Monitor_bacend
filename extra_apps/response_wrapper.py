# -*- coding:utf-8 -*-
class ResponseWrapper:

    return_code = {
         '100': 'continue',
         '101': 'switching protocols',
         '200': 'ok',
         '201': 'created',
         '202': 'accepted',
         '203': 'non authoritative information',
         '204': 'no content',
         '205': 'reset content',
         '206': 'partial content',
         '207': 'multi status',
         '300': 'multiple choices',
         '301': 'moved permanently',
         '302': 'found',
         '303': 'see other',
         '304': 'not modified',
         '305': 'use proxy',
         '306': 'reserved',
         '307': 'temporary redirect',
         '400': 'bad request',
         '401': 'unauthorized',
         '402': 'payment required',
         '403': 'forbidden',
         '404': 'not found',
         '405': 'method not allowed',
         '406': 'not acceptable',
         '407': 'proxy authentication required',
         '408': 'request timeout',
         '409': 'conflict',
         '410': 'gone',
         '411': 'length required',
         '412': 'precondition failed',
         '413': 'request entity too large',
         '414': 'request uri too long',
         '415': 'unsupported media type',
         '416': 'requested range not satisfiable',
         '417': 'expectation failed',
         '422': 'unprocessable entity',
         '423': 'locked',
         '424': 'failed dependency',
         '428': 'precondition required',
         '429': 'too many requests',
         '431': 'request header fields too large',
         '451': 'unavailable for legal reasons',
         '500': 'internal server error',
         '501': 'not implemented',
         '502': 'bad gateway',
         '503': 'service unavailable',
         '504': 'gateway timeout',
         '505': 'version not supported',
         '507': 'insufficient storage',
         '511': 'network authentication required'
    }

    __result = {'success': False, 'code': None, 'msg': None, 'data': None}

    def mark_custom(self, success, code, msg, data=None):
        '''
        自定义返回结果
        :param success:
        :param code:
        :param msg:
        :param data:
        :return:
        '''
        self.__result['success'] = success
        self.__result['code'] = code
        self.__result['msg'] = msg
        self.__result['data'] = data
        return self.__result

    def execute_success(self, data=None):
        self.__result['success'] = True
        self.__result['code'] = '200'
        self.__result['msg'] = self.return_code['200']
        self.__result['data'] = data
        return self.__result

    def authentication_failed(self):
        self.__result['success'] = False
        self.__result['code'] = '401'
        self.__result['msg'] = self.return_code['401']
        return self.__result

    def unknown_work_order_id(self):
        self.__result['success'] = False
        self.__result['code'] = '404'
        self.__result['msg'] = self.return_code['404']
        return self.__result

    def system_error(self):
        self.__result['success'] = False
        self.__result['code'] = '500'
        self.__result['msg'] = self.return_code['500']
        return self.__result

