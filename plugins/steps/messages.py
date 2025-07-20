# plugins/steps/messages.py
from airflow.providers.telegram.hooks.telegram import TelegramHook

def send_telegram_failure_message(context):
    hook = TelegramHook(token='7678217673:AAEAfN8Vgt2PNhp4MtBPK2SepvLm8T4kc0Q',
                        chat_id='-4938638858')
    run_id = context["run_id"]
    task_instance_key_str = context["task_instance_key_str"]
    
    message = f"Ошибка: run_id:{run_id}, task_instance_key_str: {task_instance_key_str}"
    
    hook.send_message({
        'chat_id': '-4938638858',
        'text': message
    })
    
def send_telegram_success_message(context): 
    hook = TelegramHook(token='7678217673:AAEAfN8Vgt2PNhp4MtBPK2SepvLm8T4kc0Q',
                        chat_id='-4938638858')
    dag = context['dag'].dag_id
    run_id = context['run_id']
    
    message = f'Исполнение DAG {dag} с id={run_id} прошло успешно!'
    hook.send_message({
        'chat_id': '{вставьте ваш chat_id}',
        'text': message
    })